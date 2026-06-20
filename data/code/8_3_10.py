def calculate_polygon_area(vertices):
    n = len(vertices)
    if n < 3:
        return 0.0
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        xi, yi = vertices[i]
        xj, yj = vertices[j]
        area += (xi * yj) - (xj * yi)
    return abs(area) / 2.0

if __name__ == '__main__':
    polygon_vertices = [(0, 0), (4, 0), (4, 4), (0, 4)]
    result = calculate_polygon_area(polygon_vertices)
    print(result)