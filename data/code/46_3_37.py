def validate_sides(side1, side2, side3):
    if not (isinstance(side1, int) and isinstance(side2, int) and isinstance(side3, int)):
        raise ValueError("All sides must be integers.")
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        raise ValueError("All sides must be positive integers.")

def calculate_triangle_perimeter(side1, side2, side3):
    validate_sides(side1, side2, side3)
    return side1 + side2 + side3

if __name__ == '__main__':
    try:
        side1 = 7
        side2 = 9
        side3 = 12
        perimeter = calculate_triangle_perimeter(side1, side2, side3)
        print(perimeter)
    except ValueError as e:
        print(e)