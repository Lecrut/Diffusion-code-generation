import turtle
def draw_triangle(x1, y1, x2, y2, x3, y3):
    t = turtle.Turtle()
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.goto(x2, y2)
    t.goto(x3, y3)
    t.hideturtle()
if __name__ == '__main__':
    draw_triangle(0, 0, 50, 0, 25, 40)