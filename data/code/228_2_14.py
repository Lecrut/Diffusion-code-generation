import turtle
ANGLE_STEP = 2 * 3.14159 / 3

def draw_equilateral_triangle(side_length):
    for _ in range(3):
        turtle.forward(side_length)
        turtle.left(ANGLE_STEP)
if __name__ == '__main__':
    side_length = 100
    turtle.speed(1)
    draw_equilateral_triangle(side_length)