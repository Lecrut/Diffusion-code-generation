import turtle
SIDE_LENGTH = 100

def draw_square():
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-SIDE_LENGTH / 2, -SIDE_LENGTH / 2)
    turtle.pendown()
    turtle.fillcolor('black')
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(SIDE_LENGTH)
        turtle.left(90)
    turtle.end_fill()
if __name__ == '__main__':
    draw_square()
    turtle.done()