import turtle

def draw_square(side_length):
    for _ in range(4):
        turtle.forward(side_length)
        turtle.left(90)
if __name__ == '__main__':
    screen = turtle.Screen()
    screen.setup(width=200, height=200, startx=-100, starty=100)
    screen.title('Solid Black Square')
    turtle.speed('fastest')
    turtle.penup()
    turtle.goto(-50, -50)
    turtle.pendown()
    draw_square(100)
    turtle.hideturtle()
    screen.mainloop()