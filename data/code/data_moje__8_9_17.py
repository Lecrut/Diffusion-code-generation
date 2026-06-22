import math

def calculate_polygon_area(vertices):
    if len(vertices) < 3:
        return 0.0
    n = len(vertices)
    area = 0.0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        area += (x1 * y2) - (x2 * y1)
    return abs(area) / 2.0

if __name__ == '__main__':
    square_vertices = [(0, 0), (4, 0), (4, 4), (0, 4)]
    triangle_vertices = [(1, 1), (4, 2), (2, 5)]
    complex_vertices = [(0, 0), (1, 0), (2, 2), (1, 3), (0, 2)]
    print(calculate_polygon_area(square_vertices))
    print(calculate_polygon_area(triangle_vertices))
    print(calculate_polygon_area(complex_vertices))