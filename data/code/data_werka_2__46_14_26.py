def is_valid_triangle(side1, side2, side3):
    return side1 > 0 and side2 > 0 and side3 > 0

def calculate_triangle_perimeter(side1, side2, side3):
    if not is_valid_triangle(side1, side2, side3):
        raise ValueError("Side lengths must be positive numbers.")
    return side1 + side2 + side3

if __name__ == '__main__':
    side1 = 6
    side2 = 8
    side3 = 10
    perimeter = calculate_triangle_perimeter(side1, side2, side3)
    print(perimeter)