import turtle

def draw_square(side_length):
    for _ in range(4):
        turtle.forward(side_length)
        turtle.left(90)
if __name__ == '__main__':
    turtle.speed(2)
    turtle.penup()
    turtle.goto(-50, 50)
    turtle.pendown()
    turtle.color('black')
    draw_square(100)