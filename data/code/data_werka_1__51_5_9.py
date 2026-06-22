def calculate_polygon_perimeter(sides):
    if not isinstance(sides, list):
        raise TypeError('Input must be a list of side lengths.')
    if any((not isinstance(side, (int, float)) for side in sides)):
        raise ValueError('All elements in the list must be numbers.')
    if len(sides) < 3:
        raise ValueError('A polygon must have at least 3 sides.')
    return sum(sides)
if __name__ == '__main__':
    polygon_sides = [3, 4, 5]
    try:
        perimeter = calculate_polygon_perimeter(polygon_sides)
        print(perimeter)
    except Exception as e:
        print(e)