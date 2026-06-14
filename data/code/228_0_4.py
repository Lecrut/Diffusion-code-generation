import turtle
def draw_triangle(side_a, side_b, side_c):
    t = turtle.Turtle()
    t.speed(1)
    t.penup()
    t.goto(-side_a / 2, -side_c / 2)
    t.pendown()
    t.setheading(90)
    t.forward(side_a)
    t.setheading(180 - (180 - 60))
    t.forward(side_b)
    t.setheading(270 - (180 - 30))
    t.forward(side_c)
if __name__ == '__main__':
    side1 = 50
    side2 = 60
    side3 = 70
    draw_triangle(side1, side2, side3)
    turtle.done