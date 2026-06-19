def calculate_area(dimensions):
    n = len(dimensions)
    if n == 3:
        return 0.5 * dimensions[0] * dimensions[1]
    elif n % 2 == 0 and n >= 4:
        area = 0
        for i in range(n // 2):
            x1, y1 = (dimensions[2 * i], dimensions[2 * i + 1])
            x2, y2 = (dimensions[2 * (i + 1) % n], dimensions[2 * (i + 1) % n + 1])
            area += x1 * y2 - y1 * x2
        return abs(area) / 2
    else:
        raise ValueError('Unsupported number of dimensions for area calculation')
if __name__ == '__main__':
    triangle_dimensions = [3, 4]
    quadrilateral_dimensions = [1, 2, 3, 4, 5, 6]
    print('Triangle area:', calculate_area(triangle_dimensions))
    print('Quadrilateral area:', calculate_area(quadrilateral_dimensions))