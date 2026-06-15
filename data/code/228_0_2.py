import turtle
def draw_triangle(t, side1, side2, side3):
    t.penup()
    t.goto(-side1 / 2, -side2 / 2)
    t.pendown()
    t.goto(side1 / 2, -side2 / 2)
    t.goto(side1 / 2 + side3 * (side1 / side2), side3 / 2)
    t.goto(-side1 / 2, side3 / 2)
if __name__ == '__main__':
    t = turtle.Turtle()
    t.speed(1)
    s1 = 50
    s2 = 60
    s3 = 70
    draw_triangle(t, s1, s2, s3)
    t.hideturtle()
    turtle.done