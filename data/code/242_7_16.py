def area_rhombus(d1, d2):
    if d1 <= 0 or d2 <= 0:
        raise ValueError("Diagonals must be positive numbers.")
    return 0.5 * d1 * d2

def area_square(side):
    if side <= 0:
        raise ValueError("Side length must be a positive number.")
    return side ** 2

if __name__ == '__main__':
    rhombus_area = area_rhombus(10, 8)
    square_area = area_square(6)
    print(f"Rhombus Area: {rhombus_area}")
    print(f"Square Area: {square_area}")