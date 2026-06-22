def area_rhombus(d1, d2):
    if not (isinstance(d1, (int, float)) and isinstance(d2, (int, float))):
        raise ValueError("Diagonals must be numbers.")
    return 0.5 * d1 * d2

def area_square(side):
    if not isinstance(side, (int, float)):
        raise ValueError("Side length must be a number.")
    return side ** 2

if __name__ == '__main__':
    rhombus_area = area_rhombus(10, 8)
    square_area = area_square(6)
    print(f"Rhombus Area: {rhombus_area}")
    print(f"Square Area: {square_area}")