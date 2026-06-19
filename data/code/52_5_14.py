def calculate_area(dimensions):
    n = len(dimensions)
    if n == 3:
        a, b, c = dimensions
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5
    elif n == 4:
        x1, y1 = (dimensions[0], dimensions[1])
        x2, y2 = (dimensions[2], dimensions[3])
        return abs(x1 * y2 - x2 * y1) / 2
    else:
        raise ValueError('Unsupported number of sides for area calculation')
if __name__ == '__main__':
    triangle_sides = [3, 4, 5]
    quadrilateral_sides = [0, 0, 4, 0, 4, 3, 0, 3]
    print('Area of triangle:', calculate_area(triangle_sides))
    print('Area of quadrilateral:', calculate_area(quadrilateral_sides))