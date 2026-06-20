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
    area = abs(area) / 2.0
    if area < 1e-9:
        return 0.0
    return area

if __name__ == '__main__':
    sample_vertices = [(0, 0), (4, 0), (4, 3), (0, 3)]
    result = calculate_polygon_area(sample_vertices)
    print(result)