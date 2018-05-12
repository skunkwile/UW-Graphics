import display
from algebra import Vec3, Mat3
from engine import *
import time

size = width, height = 640, 480

scene = Scene()

camera = Camera(0.1, 640, 480, 1, 100)
scene.primary_camera = camera
scene.root.add_child(camera)

# mesh = Mesh([
#     Vec3(-10, 0, 0),
#     Vec3(0, 0, -5),
#     Vec3(3, 0, 7),
#     Vec3(4, 0, 1),
# ], [(1, 2, 3), (0, 1, 2)])
mesh = Mesh([
    Vec3(-1, 1, 1),  # Back Left Top
    Vec3(-1, 1, -1),  # Back Left Bottom
    Vec3(1, 1, -1),  # Back Right Bottom
    Vec3(1, 1, 1),  # Back Right Top
    Vec3(-1, -1, 1),  # Front Left Top
    Vec3(-1, -1, -1),  # Front Left Bottom
    Vec3(1, -1, -1),  # Front Right Bottom
    Vec3(1, -1, 1),  # Front Right Top
], [
    # (0, 3, 4), (0, 4, 7),
    (1, 2, 5), (2, 5, 6),
    # (0, 1, 5), (0, 4, 5),
    (3, 2, 6), (3, 7, 6),
    (4, 7, 6), (4, 6, 5),
    # (0, 3, 2), (0, 3, 1),

    # (0, 1, 2), (0, 2, 3),  # BACK
    # (1, 2, 5), (5, 2, 6),  # LEFT
    # (4, 5, 6), (4, 6, 7),  # BOTTOM
    # (3, 4, 7), (4, 0, 3),  # TOP
    # (6, 2, 3),
    # (3, 6, 7),  # RIGHT
    # (0, 1, 4),
    # (1, 4, 5),  # LEFT
])

node = Node(mesh, Transform.make(Vec3(0, 5, 0), Vec3(-0.6, 0.8, -0.5), Vec3(9, 1, 9)))
scene.root.add_child(node)

camera = Camera(50, 500, 500, 1, 20)
scene.root.add_child(camera)
scene.primary_camera = camera

# i = 0


def main_loop(screen):
    # global i
    # time.sleep(0.05)
    screen.draw(scene.render())
    # scene.render()
    # i += 1


display.Screen(*size, title="UW Graphics", update=main_loop)