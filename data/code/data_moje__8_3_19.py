def polygon_area(vertices):
    if len(vertices) < 3:
        return 0.0
    n = len(vertices)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        x_i, y_i = vertices[i]
        x_j, y_j = vertices[j]
        area += x_i * y_j - x_j * y_i
    return abs(area) / 2.0

if __name__ == '__main__':
    square = [(0, 0), (4, 0), (4, 4), (0, 4)]
    triangle = [(0, 0), (5, 0), (2, 3)]
    pentagon = [(1, 1), (3, 1), (4, 3), (2, 5), (0, 3)]
    print(polygon_area(square))
    print(polygon_area(triangle))
    print(polygon_area(pentagon))