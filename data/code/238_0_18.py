import turtle

def draw_square(side_length):
    for _ in range(4):
        turtle.forward(side_length)
        turtle.left(90)

def main():
    side_length = 100
    turtle.speed(2)
    turtle.penup()
    turtle.goto(-side_length / 2, side_length / 2)
    turtle.pendown()
    draw_square(side_length)
    turtle.done()
if __name__ == '__main__':
    main()