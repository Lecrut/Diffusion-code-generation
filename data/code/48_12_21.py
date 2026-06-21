import math

def calculate_equilateral_triangle_sides_and_perimeter(height):
    side_length = 2 * height / math.sqrt(3)
    perimeter = 3 * side_length
    return (side_length, perimeter)
if __name__ == '__main__':
    height = 8.73
    side_length, perimeter = calculate_equilateral_triangle_sides_and_perimeter(height)
    print(f'Side Length: {side_length:.2f}')
    print(f'Perimeter: {perimeter:.2f}')