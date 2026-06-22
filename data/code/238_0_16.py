import turtle

def draw_square(side_length):
    if side_length <= 0:
        raise ValueError("Side length must be greater than zero.")
    
    turtle.speed(1)
    turtle.penup()
    turtle.goto(-side_length / 2, side_length / 2)
    turtle.pendown()
    turtle.fillcolor("black")
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(side_length)
        turtle.right(90)
    turtle.end_fill()

if __name__ == '__main__':
    draw_square(100)