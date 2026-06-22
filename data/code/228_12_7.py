import turtle
SIDE_LENGTH = 100

def draw_triangle(side_length):
    for _ in range(3):
        turtle.forward(side_length)
        turtle.left(120)
if __name__ == '__main__':
    turtle.speed(1)
    draw_triangle(SIDE_LENGTH)
    turtle.done()