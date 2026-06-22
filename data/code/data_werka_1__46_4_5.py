def validate_sides(side1, side2, side3):
    if not (side1 > 0 and side2 > 0 and side3 > 0):
        raise ValueError("Side lengths must be positive integers")
    if not (side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1):
        raise ValueError("Invalid triangle sides")

def calculate_triangle_perimeter(side1, side2, side3):
    validate_sides(side1, side2, side3)
    return side1 + side2 + side3

if __name__ == '__main__':
    side1 = 7
    side2 = 24
    side3 = 25
    perimeter = calculate_triangle_perimeter(side1, side2, side3)
    print(perimeter)