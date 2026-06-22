import math

def calculate_side_length_from_height(height):
    return (2 * height) / math.sqrt(3)

def calculate_perimeter_from_side_length(side_length):
    return 3 * side_length

if __name__ == '__main__':
    triangle_height = 8.73
    side_length = calculate_side_length_from_height(triangle_height)
    perimeter = calculate_perimeter_from_side_length(side_length)
    print(f"Side Length: {side_length:.2f}")
    print(f"Perimeter: {perimeter:.2f}")