def is_valid_triangle_side(side):
    return side > 0

def validate_triangle_sides(sides):
    if len(sides) != 3:
        raise ValueError('Exactly three sides are required.')
    if not all((is_valid_triangle_side(side) for side in sides)):
        raise ValueError('All sides must be positive numbers.')

def calculate_perimeter(sides):
    validate_triangle_sides(sides)
    return sum(sides)
if __name__ == '__main__':
    try:
        valid_sides = [3, 4, 5]
        perimeter = calculate_perimeter(valid_sides)
        print(perimeter)
    except ValueError as e:
        print(f'Error: {e}')
    invalid_sides_zero = [3, 0, 5]
    try:
        perimeter = calculate_perimeter(invalid_sides_zero)
        print(perimeter)
    except ValueError as e:
        print(f'Error: {e}')
    invalid_sides_negative = [3, -4, 5]
    try:
        perimeter = calculate_perimeter(invalid_sides_negative)
        print(perimeter)
    except ValueError as e:
        print(f'Error: {e}')