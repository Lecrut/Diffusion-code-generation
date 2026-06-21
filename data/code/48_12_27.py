import math

def calculate_side_length_from_height(height):
    return (2 * height) / math.sqrt(3)

def calculate_perimeter(side_length):
    return 3 * side_length

def get_triangle_properties(height):
    if height <= 0:
        raise ValueError("Height must be positive")
    
    side_length = calculate_side_length_from_height(height)
    perimeter = calculate_perimeter(side_length)
    return (side_length, perimeter)

if __name__ == '__main__':
    sample_height = 8.73
    try:
        side_length, perimeter = get_triangle_properties(sample_height)
        print(f'Side Length: {side_length:.2f}')
        print(f'Perimeter: {perimeter:.2f}')
    except ValueError as e:
        print(e)