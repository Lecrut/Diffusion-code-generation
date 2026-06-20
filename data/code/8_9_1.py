def calculate_polygon_area(vertices):
    n = len(vertices)
    if n < 3:
        return 0.0
    area = 0.0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        area += x1 * y2
        area -= x2 * y1
    area = abs(area) / 2.0
    return round(area, 10)

if __name__ == '__main__':
    square_vertices = [(0, 0), (4, 0), (4, 4), (0, 4)]
    triangle_vertices = [(0, 0), (6, 0), (3, 9)]
    irregular_vertices = [(1, 1), (4, 2), (3, 5), (1, 3)]
    print(calculate_polygon_area(square_vertices))
    print(calculate_polygon_area(triangle_vertices))
    print(calculate_polygon_area(irregular_vertices))