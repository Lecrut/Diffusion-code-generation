import math
def generate_equilateral_triangle(radius):
    angle = 2 * math.pi / 3
    vertices = [
        (radius * math.cos(0), radius * math.sin(0)),
        (radius * math.cos(angle), radius * math.sin(angle)),
        (radius * math.cos(2 * angle), radius * math.sin(2 * angle))
    ]
    return vertices
if __name__ == '__main__':
    sample_radius = 5.0
    triangle_vertices = generate_equilateral_triangle(sample_radius)
    print(triangle_vertices)