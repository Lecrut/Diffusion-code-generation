import math

def calculate_polygon_area(vertices):
    n = len(vertices)
    if n < 3:
        return 0.0
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]
    return abs(area) / 2.0

if __name__ == '__main__':
    square_vertices = [(0, 0), (0, 4), (4, 4), (4, 0)]
    triangle_vertices = [(0, 0), (4, 0), (0, 3)]
    square_area = calculate_polygon_area(square_vertices)
    triangle_area = calculate_polygon_area(triangle_vertices)
    print(square_area)
    print(triangle_area)