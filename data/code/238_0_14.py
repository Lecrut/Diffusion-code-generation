import turtle

def draw_square(side_length):
    for _ in range(4):
        turtle.forward(side_length)
        turtle.left(90)

def main():
    if not isinstance((side_length := 100), (int, float)) or side_length <= 0:
        raise ValueError('Side length must be a positive number')
    screen = turtle.Screen()
    screen.setup(width=200, height=200)
    screen.bgcolor('white')
    pen = turtle.Turtle()
    pen.speed(0)
    pen.penup()
    pen.goto(-side_length / 2, side_length / 2)
    pen.pendown()
    pen.color('black', 'black')
    draw_square(side_length)
    pen.hideturtle()
    screen.mainloop()
if __name__ == '__main__':
    main()