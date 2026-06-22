import turtle

SIDE_LENGTH = 100
ANGLE = 120

def draw_triangle():
    for _ in range(3):
        turtle.forward(SIDE_LENGTH)
        turtle.left(ANGLE)

if __name__ == '__main__':
    turtle.speed(1)
    draw_triangle()
    turtle.done()