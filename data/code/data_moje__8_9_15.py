def calculate_polygon_area(vertices):
    if len(vertices) < 3:
        return 0.0
    n = len(vertices)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        x1, y1 = vertices[i]
        x2, y2 = vertices[j]
        area += x1 * y2 - x2 * y1
    area = abs(area) / 2.0
    return round(area, 10)

if __name__ == '__main__':
    square = [(0, 0), (1, 0), (1, 1), (0, 1)]
    triangle = [(0, 0), (4, 0), (0, 3)]
    irregular = [(1, 1), (5, 1), (5, 5), (2, 6), (1, 3)]
    print(calculate_polygon_area(square))
    print(calculate_polygon_area(triangle))
    print(calculate_polygon_area(irregular))