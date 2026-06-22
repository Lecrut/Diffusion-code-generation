import turtle

def draw_equilateral_triangle(side_length):
    for _ in range(3):
        turtle.forward(side_length)
        turtle.left(120)

if __name__ == '__main__':
    side_length = 100
    turtle.speed(2)
    turtle.penup()
    turtle.goto(-50, -50)
    turtle.pendown()
    draw_equilateral_triangle(side_length)