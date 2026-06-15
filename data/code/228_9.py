import turtle
def draw_triangle(vertices):
    t = turtle.Turtle()
    t.speed(1)
    t.penup()
    t.goto(vertices[0][0], vertices[0][1])
    t.pendown()
    for i in range(2):
        t.goto(vertices[i+1][0], vertices[i+1][1])
    t.goto(vertices[0][0], vertices[0][1])
if __name__ == '__main__':
    vertices = [
        (0, 0),
        (4, 0),
        (2, 3)
    ]
    draw_triangle(vertices)
    turtle.done