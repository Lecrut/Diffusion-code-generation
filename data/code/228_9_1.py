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
    vertex1 = (0, 0)
    vertex2 = (5, 0)
    vertex3 = (2.5, 4)
    triangle_vertices = [vertex1, vertex2, vertex3]
    draw_triangle(triangle_vertices)
    turtle.done