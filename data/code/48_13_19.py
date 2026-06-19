import math
SQRT_3 = math.sqrt(3)

def calculate_equilateral_triangle_properties(height):
    side_length = 2 * height / SQRT_3
    perimeter = 3 * side_length
    return (side_length, perimeter)
if __name__ == '__main__':
    height = 8.73
    side_length, perimeter = calculate_equilateral_triangle_properties(height)
    print(f'Side Length: {side_length}')
    print(f'Perimeter: {perimeter}')