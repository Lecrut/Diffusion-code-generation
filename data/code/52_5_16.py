def calculate_area(dimensions):
    n = len(dimensions)
    if n == 3:
        a, b, c = dimensions
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5
    elif n == 4:
        x1, y1, x2, y2, x3, y3, x4, y4 = dimensions
        return abs((x1 * y2 + x2 * y3 + x3 * y4 + x4 * y1 - y1 * x2 - y2 * x3 - y3 * x4 - y4 * x1) / 2)
    else:
        area = 0
        for i in range(0, n, 2):
            j = (i + 2) % n
            area += dimensions[i] * dimensions[j + 1]
            area -= dimensions[j] * dimensions[i + 1]
        return abs(area) / 2
if __name__ == '__main__':
    triangle_dimensions = [3, 4, 5]
    quadrilateral_dimensions = [0, 0, 4, 0, 4, 3, 0, 3]
    polygon_dimensions = [1, 0, 2, 0, 2, 3, 1, 3]
    print('Triangle area:', calculate_area(triangle_dimensions))
    print('Quadrilateral area:', calculate_area(quadrilateral_dimensions))
    print('Polygon area:', calculate_area(polygon_dimensions))