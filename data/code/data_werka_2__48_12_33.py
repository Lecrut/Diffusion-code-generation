import math

def validate_height(height):
    if height <= 0:
        raise ValueError("Height must be positive")

def calculate_side_length_from_height(height):
    return (2 * height) / math.sqrt(3)

def calculate_perimeter_from_side_length(side_length):
    return 3 * side_length

def calculate_equilateral_triangle_sides_and_perimeter(height):
    validate_height(height)
    side_length = calculate_side_length_from_height(height)
    perimeter = calculate_perimeter_from_side_length(side_length)
    return (side_length, perimeter)

if __name__ == '__main__':
    height = 8.73
    try:
        side_length, perimeter = calculate_equilateral_triangle_sides_and_perimeter(height)
        print(f'Side Length: {side_length:.2f}')
        print(f'Perimeter: {perimeter:.2f}')
    except ValueError as e:
        print(e)