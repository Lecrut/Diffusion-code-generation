def calculate_polygon_area(vertices):
    n = len(vertices)
    if n < 3:
        return 0.0

    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        xi, yi = vertices[i]
        xj, yj = vertices[j]
        area += xi * yj
        area -= xj * yi

    area = abs(area) / 2.0
    return round(area, 10)

if __name__ == '__main__':
    square = [(0, 0), (1, 0), (1, 1), (0, 1)]
    triangle = [(0, 0), (4, 0), (2, 3)]
    pentagon = [(1, 1), (3, 0), (5, 1), (4, 3), (2, 3)]

    print(calculate_polygon_area(square))
    print(calculate_polygon_area(triangle))
    print(calculate_polygon_area(pentagon))