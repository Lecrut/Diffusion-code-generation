def calculate_polygon_area(vertices):
    if not vertices or len(vertices) < 3:
        return 0.0
    n = len(vertices)
    total = 0.0
    for i in range(n):
        j = (i + 1) % n
        x1, y1 = vertices[i]
        x2, y2 = vertices[j]
        total += x1 * y2 - x2 * y1
    area = abs(total) / 2.0
    return round(area, 10)

if __name__ == '__main__':
    square_vertices = [(0, 0), (1, 0), (1, 1), (0, 1)]
    triangle_vertices = [(0, 0), (4, 0), (0, 3)]
    irregular_vertices = [(0, 0), (4, 0), (5, 3), (2, 5), (0, 3)]
    print(calculate_polygon_area(square_vertices))
    print(calculate_polygon_area(triangle_vertices))
    print(calculate_polygon_area(irregular_vertices))
    print(calculate_polygon_area([]))
    print(calculate_polygon_area([(1, 1)]))
    print(calculate_polygon_area([(0, 0), (1, 1)]))