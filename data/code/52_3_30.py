def calculate_area(dimensions):
    if len(dimensions) == 3:
        a, b, c = dimensions
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5
    elif len(dimensions) == 4:
        x1, y1, x2, y2 = dimensions
        return abs(x1 * y2 - x2 * y1) / 2
    else:
        raise ValueError('Unsupported number of dimensions for area calculation')
if __name__ == '__main__':
    triangle_dimensions = [3, 4, 5]
    quadrilateral_dimensions = [0, 0, 4, 0]
    print('Area of triangle:', calculate_area(triangle_dimensions))
    print('Area of quadrilateral:', calculate_area(quadrilateral_dimensions))