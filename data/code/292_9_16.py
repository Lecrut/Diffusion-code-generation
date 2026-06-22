def validate_sides(side1, side2):
    if not (isinstance(side1, (int, float)) and isinstance(side2, (int, float))):
        raise ValueError("Sides must be numbers")
    if side1 <= 0 or side2 <= 0:
        raise ValueError("Sides must be positive")

def calculate_perimeter(side1, side2):
    validate_sides(side1, side2)
    return 2 * (side1 + side2)

if __name__ == '__main__':
    print(calculate_perimeter(5, 7))