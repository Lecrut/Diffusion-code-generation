def calculate_area(dimensions):
    if len(dimensions) == 3:
        a, b, c = dimensions
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5
    elif len(dimensions) == 4:
        x1, y1 = (dimensions[0], dimensions[1])
        x2, y2 = (dimensions[2], dimensions[3])
        return abs(x1 * y2 - x2 * y1) / 2
    else:
        raise ValueError('Unsupported number of dimensions for area calculation.')
if __name__ == '__main__':
    triangle_dimensions = [3, 4, 5]
    quadrilateral_dimensions = [(0, 0), (4, 0), (4, 3), (0, 3)]
    try:
        triangle_area = calculate_area(triangle_dimensions)
        print(f'Area of triangle with dimensions {triangle_dimensions}: {triangle_area}')
    except ValueError as e:
        print(f'Error: {e}')
    try:
        quadrilateral_area = calculate_area(quadrilateral_dimensions)
        print(f'Area of quadrilateral with dimensions {quadrilateral_dimensions}: {quadrilateral_area}')
    except ValueError as e:
        print(f'Error: {e}')