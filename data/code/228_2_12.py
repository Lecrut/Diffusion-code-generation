import turtle

def draw_equilateral_triangle(side_length):
    for _ in range(3):
        turtle.forward(side_length)
        turtle.left(120)

if __name__ == '__main__':
    side_length = 100
    turtle.speed('fastest')
    turtle.penup()
    turtle.goto(-side_length / 2, 0)
    turtle.pendown()
    draw_equilateral_triangle(side_length)