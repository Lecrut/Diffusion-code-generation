MIN_SIDE_LENGTH = 1

def calculate_triangle_perimeter(side1, side2, side3):
    if side1 < MIN_SIDE_LENGTH or side2 < MIN_SIDE_LENGTH or side3 < MIN_SIDE_LENGTH:
        raise ValueError("Side lengths must be positive numbers.")
    return side1 + side2 + side3

if __name__ == '__main__':
    side1 = 6
    side2 = 8
    side3 = 10
    perimeter = calculate_triangle_perimeter(side1, side2, side3)
    print(perimeter)