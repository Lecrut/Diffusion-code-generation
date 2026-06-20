import math

def calculate_polygon_area(vertices):
    if len(vertices) < 3:
        return 0.0
    n = len(vertices)
    total = 0.0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        total += (x1 * y2) - (x2 * y1)
    area = abs(total) / 2.0
    return round(area, 10)

if __name__ == '__main__':
    sample_vertices = [(0, 0), (4, 0), (4, 3), (0, 3)]
    result = calculate_polygon_area(sample_vertices)
    print(result)
    sample_triangle = [(1, 1), (4, 5), (7, 1)]
    result_triangle = calculate_polygon_area(sample_triangle)
    print(result_triangle)