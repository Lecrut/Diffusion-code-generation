import math

def validate_height(height):
    if height <= 0:
        raise ValueError("Height must be positive")

def calculate_side_length_from_height(height):
    return 2 * height / math.sqrt(3)

def calculate_perimeter(side_length):
    return 3 * side_length

def calculate_equilateral_triangle_properties(height):
    validate_height(height)
    side_length = calculate_side_length_from_height(height)
    perimeter = calculate_perimeter(side_length)
    return (side_length, perimeter)

if __name__ == '__main__':
    height = 8.73
    try:
        side_length, perimeter = calculate_equilateral_triangle_properties(height)
        print(f'Side Length: {side_length}')
        print(f'Perimeter: {perimeter}')
    except ValueError as e:
        print(e)