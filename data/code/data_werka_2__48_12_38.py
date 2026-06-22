import math
SQRT_3 = math.sqrt(3)

def calculate_side_length(height):
    return 2 * height / SQRT_3

def calculate_perimeter(side_length):
    return 3 * side_length
if __name__ == '__main__':
    height = 8.73
    try:
        side_length = calculate_side_length(height)
        perimeter = calculate_perimeter(side_length)
        print(f'Side Length: {side_length:.2f}')
        print(f'Perimeter: {perimeter:.2f}')
    except ValueError as e:
        print(e)