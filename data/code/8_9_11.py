def calculate_polygon_area(vertices):
    n = len(vertices)
    if n < 3:
        return 0.0
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]
    area = abs(area) / 2.0
    if area < 1e-9:
        return 0.0
    return area

if __name__ == '__main__':
    square = [(0, 0), (1, 0), (1, 1), (0, 1)]
    print(calculate_polygon_area(square))
    triangle = [(0, 0), (4, 0), (2, 3)]
    print(calculate_polygon_area(triangle))
    pentagon = [(1, 1), (4, 1), (5, 3), (3, 5), (0, 3)]
    print(calculate_polygon_area(pentagon))