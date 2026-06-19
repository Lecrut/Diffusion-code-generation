def determine_polygon_type_and_semi_perimeter(sides):
    num_sides = len(sides)
    if num_sides < 3:
        return ('Not a polygon', None)
    elif num_sides == 3:
        polygon_type = 'Triangle'
    elif num_sides == 4:
        polygon_type = 'Quadrilateral'
    else:
        polygon_type = f'{num_sides}-sided polygon'
    semi_perimeter = sum(sides) / 2
    return (polygon_type, semi_perimeter)
if __name__ == '__main__':
    side_lengths = [5, 12, 13]
    polygon_type, semi_perimeter = determine_polygon_type_and_semi_perimeter(side_lengths)
    print(f'Polygon Type: {polygon_type}')
    print(f'Semi-perimeter: {semi_perimeter}')
    side_lengths_quadrilateral = [10, 20, 30, 40]
    polygon_type, semi_perimeter = determine_polygon_type_and_semi_perimeter(side_lengths_quadrilateral)
    print(f'Polygon Type: {polygon_type}')
    print(f'Semi-perimeter: {semi_perimeter}')
    side_lengths_pentagon = [1, 2, 3, 4, 5]
    polygon_type, semi_perimeter = determine_polygon_type_and_semi_perimeter(side_lengths_pentagon)
    print(f'Polygon Type: {polygon_type}')
    print(f'Semi-perimeter: {semi_perimeter}')