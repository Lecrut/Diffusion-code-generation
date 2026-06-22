def validate_diagonals(d1, d2):
    if not all(isinstance(i, (int, float)) for i in [d1, d2]):
        raise ValueError("Diagonals must be numbers")
    if d1 <= 0 or d2 <= 0:
        raise ValueError("Diagonals must be positive")

def validate_side_length(side):
    if not isinstance(side, (int, float)):
        raise ValueError("Side length must be a number")
    if side <= 0:
        raise ValueError("Side length must be positive")

def area_rhombus(d1, d2):
    validate_diagonals(d1, d2)
    return 0.5 * d1 * d2

def area_square(side):
    validate_side_length(side)
    return side ** 2

if __name__ == '__main__':
    rhombus_area = area_rhombus(10, 8)
    square_area = area_square(6)
    print(f"Rhombus Area: {rhombus_area}")
    print(f"Square Area: {square_area}")