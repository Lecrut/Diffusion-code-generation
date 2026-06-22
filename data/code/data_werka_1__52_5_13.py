def calculate_polygon_area(dimensions):
    if not dimensions or len(dimensions) < 3:
        raise ValueError('Dimensions must be a list of at least three sides.')
    if any((side <= 0 for side in dimensions)):
        raise ValueError('All sides must be positive values.')
    n = len(dimensions)
    area = 0.5 * abs(sum((dimensions[i] * dimensions[(i + 1) % n] - dimensions[(i + 1) % n] * dimensions[i] for i in range(n))))
    return area
if __name__ == '__main__':
    try:
        polygon_dimensions_1 = [3, 4, 5]
        area_1 = calculate_polygon_area(polygon_dimensions_1)
        print(f'Area of polygon with sides {polygon_dimensions_1}: {area_1}')
        polygon_dimensions_2 = [0, 4, 5]
        area_2 = calculate_polygon_area(polygon_dimensions_2)
        print(f'Area of polygon with sides {polygon_dimensions_2}: {area_2}')
    except ValueError as e:
        print(f'Error: {e}')