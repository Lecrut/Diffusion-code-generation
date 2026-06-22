import turtle

def draw_black_square(side_length):
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-side_length / 2, side_length / 2)
    turtle.pendown()
    for _ in range(4):
        turtle.forward(side_length)
        turtle.right(90)

if __name__ == '__main__':
    draw_black_square(100)