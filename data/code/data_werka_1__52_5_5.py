def calculate_polygon_area(dimensions):
    if len(dimensions) < 3:
        raise ValueError('A polygon must have at least 3 sides.')
    if len(dimensions) == 3:
        base = dimensions[0]
        height = dimensions[1]
        return 0.5 * base * height
    area = 0
    n = len(dimensions)
    for i in range(n):
        x1, y1 = dimensions[i]
        x2, y2 = dimensions[(i + 1) % n]
        area += x1 * y2 - y1 * x2
    return abs(area) / 2
if __name__ == '__main__':
    triangle_dimensions = [4, 5]
    try:
        triangle_area = calculate_polygon_area(triangle_dimensions)
        print(f'Triangle area: {triangle_area}')
    except ValueError as e:
        print(f'Error: {e}')
    rectangle_dimensions = [(0, 0), (4, 0), (4, 3), (0, 3)]
    try:
        rectangle_area = calculate_polygon_area(rectangle_dimensions)
        print(f'Rectangle area: {rectangle_area}')
    except ValueError as e:
        print(f'Error: {e}')
    pentagon_dimensions = [(0, 0), (4, 0), (5, 3), (3, 6), (-1, 3)]
    try:
        pentagon_area = calculate_polygon_area(pentagon_dimensions)
        print(f'Pentagon area: {pentagon_area}')
    except ValueError as e:
        print(f'Error: {e}')
    invalid_dimensions = [2]
    try:
        invalid_area = calculate_polygon_area(invalid_dimensions)
        print(f'Invalid area: {invalid_area}')
    except ValueError as e:
        print(f'Error: {e}')