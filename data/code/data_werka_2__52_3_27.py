def calculate_area(dimensions):
    n = len(dimensions)
    if n == 3:
        a, b, c = dimensions
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return area
    elif n == 4:
        x1, y1, x2, y2, x3, y3, x4, y4 = dimensions
        area = abs((x1 * y2 + x2 * y3 + x3 * y4 + x4 * y1 - y1 * x2 - y2 * x3 - y3 * x4 - y4 * x1) / 2)
        return area
    else:
        raise ValueError('Unsupported number of dimensions for area calculation')
if __name__ == '__main__':
    triangle_dimensions = [3, 4, 5]
    quadrilateral_dimensions = [0, 0, 4, 0, 4, 3, 0, 3]
    print('Area of triangle:', calculate_area(triangle_dimensions))
    print('Area of quadrilateral:', calculate_area(quadrilateral_dimensions))