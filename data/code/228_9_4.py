import turtle
def draw_triangle(vertices):
    t = turtle.Turtle()
    t.speed(1)
    for x, y in vertices:
        t.penup()
        t.goto(x, y)
        t.pendown()
    t.hideturtle()
if __name__ == '__main__':
    vertices = [(-100, 0), (0, 100), (100, 0)]
    draw_triangle(vertices)