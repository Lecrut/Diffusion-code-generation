import math

def calculate_side_length_from_height(height):
    return 2 * height / math.sqrt(3)

def calculate_perimeter(side_length):
    return 3 * side_length

if __name__ == '__main__':
    height = 8.73
    side_length = calculate_side_length_from_height(height)
    perimeter = calculate_perimeter(side_length)
    print(f'Side Length: {side_length}')
    print(f'Perimeter: {perimeter}')