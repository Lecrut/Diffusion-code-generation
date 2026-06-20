def calculate_polygon_area(vertices: list) -> float:
    n = len(vertices)
    if n < 3:
        return 0.0
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        xi, yi = vertices[i]
        xj, yj = vertices[j]
        area += xi * yj
        area -= yi * xj
    return abs(area) / 2.0
if __name__ == '__main__':
    triangle = [(0, 0), (4, 0), (0, 3)]
    print(calculate_polygon_area(triangle))
    square = [(0, 0), (0, 2), (2, 2), (2, 0)]
    print(calculate_polygon_area(square))
    quad = [(1.5, 0.5), (2.5, 1.5), (1.5, 2.5), (0.5, 1.5)]
    print(calculate_polygon_area(quad))
    rectangle = [(0, 0), (0, 5), (10, 5), (10, 0)]
    print(calculate_polygon_area(rectangle))