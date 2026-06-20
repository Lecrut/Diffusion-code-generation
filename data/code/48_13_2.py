import math

def equilateral_triangle_from_height(height):
    side_length = 2 * height / math.sqrt(3)
    perimeter = 3 * side_length
    return side_length, perimeter

if __name__ == '__main__':
    side, perimeter = equilateral_triangle_from_height(8.73)
    print(side)
    print(perimeter)