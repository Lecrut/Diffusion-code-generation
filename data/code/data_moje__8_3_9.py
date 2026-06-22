def calculate_polygon_area(vertices):
    n = len(vertices)
    if n < 3:
        return 0.0
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        xi, yi = vertices[i]
        xj, yj = vertices[j]
        area += (xi * yj - xj * yi)
    return abs(area) / 2.0

if __name__ == '__main__':
    vertices = [(1, 1), (4, 1), (4, 4), (1, 4)]
    result = calculate_polygon_area(vertices)
    print(result)