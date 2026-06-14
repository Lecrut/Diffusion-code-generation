import math
def generate_equilateral_triangle(radius):
    angle_step = 2 * math.pi / 3
    vertices = []
    for i in range(3):
        angle = i * angle_step
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        vertices.append((x, y))
    return vertices
if __name__ == '__main__':
    R = 5.0
    triangle_vertices = generate_equilateral_triangle(R)
    print(triangle_vertices)