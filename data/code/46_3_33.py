def validate_sides(side1, side2, side3):
    if not all(isinstance(x, int) and x > 0 for x in (side1, side2, side3)):
        raise ValueError("All sides must be positive integers.")

def calculate_triangle_perimeter(side1, side2, side3):
    validate_sides(side1, side2, side3)
    return side1 + side2 + side3

if __name__ == '__main__':
    side1 = 7
    side2 = 9
    side3 = 12
    perimeter = calculate_triangle_perimeter(side1, side2, side3)
    print(perimeter)