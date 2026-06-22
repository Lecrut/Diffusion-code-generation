def determine_polygon_type_and_semi_perimeter(sides):
    if len(sides) < 3:
        raise ValueError('A polygon must have at least 3 sides.')
    num_sides = len(sides)
    semi_perimeter = sum(sides) / 2

    def get_polygon_type(num_sides):
        if num_sides == 3:
            return 'Triangle'
        elif num_sides == 4:
            return 'Quadrilateral'
        else:
            return f'{num_sides}-sided polygon'
    polygon_type = get_polygon_type(num_sides)
    return (polygon_type, semi_perimeter)
if __name__ == '__main__':
    sides_triangle = [3, 4, 5]
    sides_quadrilateral = [2, 2, 3, 3]
    sides_pentagon = [1, 2, 3, 4, 5]
    try:
        polygon_type_triangle, semi_perimeter_triangle = determine_polygon_type_and_semi_perimeter(sides_triangle)
        print(f'Polygon type: {polygon_type_triangle}, Semi-perimeter: {semi_perimeter_triangle}')
    except ValueError as e:
        print(e)
    try:
        polygon_type_quadrilateral, semi_perimeter_quadrilateral = determine_polygon_type_and_semi_perimeter(sides_quadrilateral)
        print(f'Polygon type: {polygon_type_quadrilateral}, Semi-perimeter: {semi_perimeter_quadrilateral}')
    except ValueError as e:
        print(e)
    try:
        polygon_type_pentagon, semi_perimeter_pentagon = determine_polygon_type_and_semi_perimeter(sides_pentagon)
        print(f'Polygon type: {polygon_type_pentagon}, Semi-perimeter: {semi_perimeter_pentagon}')
    except ValueError as e:
        print(e)