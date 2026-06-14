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
    v1 = (0, 0)
    v2 = (4, 0)
    v3 = (2, 3)
    vertices = [v1, v2, v3]
    draw_triangle(vertices)
    turtle.done