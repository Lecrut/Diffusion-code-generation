import math

def calculate_polygon_area(vertices):
    if len(vertices) < 3:
        return 0.0
    n = len(vertices)
    total = 0.0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        total += x1 * y2 - x2 * y1
    return abs(total) / 2.0

if __name__ == '__main__':
    square_vertices = [(0, 0), (1, 0), (1, 1), (0, 1)]
    triangle_vertices = [(0, 0), (4, 0), (2, 3)]
    pentagon_vertices = [
        (1, 0),
        (0.809, 0.588),
        (-0.309, 0.951),
        (-0.809, 0.588),
        (-0.5, -0.866)
    ]
    print(calculate_polygon_area(square_vertices))
    print(calculate_polygon_area(triangle_vertices))
    print(calculate_polygon_area(pentagon_vertices))