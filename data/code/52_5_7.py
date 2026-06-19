def calculate_area(dimensions):
    n = len(dimensions)
    if n == 3:
        a, b, c = dimensions
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5
    elif n % 2 == 0:
        area = 0
        for i in range(0, n, 2):
            x1, y1 = (dimensions[i], dimensions[i + 1])
            x2, y2 = (dimensions[(i + 2) % n], dimensions[(i + 3) % n])
            area += x1 * y2 - y1 * x2
        return abs(area) / 2
    else:
        raise ValueError('Unsupported number of dimensions for area calculation')
if __name__ == '__main__':
    triangle_dimensions = [3, 4, 5]
    polygon_dimensions = [0, 0, 4, 0, 4, 3, 0, 3]
    print('Triangle Area:', calculate_area(triangle_dimensions))
    print('Polygon Area:', calculate_area(polygon_dimensions))