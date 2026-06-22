import turtle
SIDE_LENGTH = 100

def draw_equilateral_triangle(side_length):
    angle_step = 2 * 3.14159 / 3
    vertices = []
    for i in range(3):
        angle = i * angle_step
        x = side_length * (0.5 if i == 0 else -0.5) * math.cos(angle)
        y = side_length * (math.sqrt(3) / 2) * math.sin(angle)
        vertices.append((x, y))
    turtle.penup()
    turtle.goto(vertices[0])
    turtle.pendown()
    for vertex in vertices:
        turtle.goto(vertex)
    turtle.goto(vertices[0])
if __name__ == '__main__':
    draw_equilateral_triangle(SIDE_LENGTH)
    turtle.done()