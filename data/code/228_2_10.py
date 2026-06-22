import turtle
SIDE_LENGTH = 100
ANGULAR_STEP = 2 * 3.14159 / 3

def draw_equilateral_triangle(side_length):
    turtle.penup()
    turtle.goto(-side_length / 2, 0)
    turtle.pendown()
    for _ in range(3):
        turtle.forward(side_length)
        turtle.left(ANGULAR_STEP)
if __name__ == '__main__':
    draw_equilateral_triangle(SIDE_LENGTH)