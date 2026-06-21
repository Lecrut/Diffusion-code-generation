def calculate_triangle_perimeter(side1, side2, side3):
    MIN_SIDE_LENGTH = 0
    if side1 <= MIN_SIDE_LENGTH or side2 <= MIN_SIDE_LENGTH or side3 <= MIN_SIDE_LENGTH:
        raise ValueError("Side lengths must be positive numbers.")
    return side1 + side2 + side3

if __name__ == '__main__':
    SAMPLE_SIDES = (6, 8, 10)
    perimeter = calculate_triangle_perimeter(*SAMPLE_SIDES)
    print(perimeter)