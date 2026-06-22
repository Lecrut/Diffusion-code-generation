def calculate_triangle_perimeter(side1, side2, side3):
    if not (isinstance(side1, (int, float)) and isinstance(side2, (int, float)) and isinstance(side3, (int, float))):
        raise ValueError("All sides must be numbers")
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        raise ValueError("All sides must be positive numbers")
    return side1 + side2 + side3

if __name__ == '__main__':
    side1 = 7
    side2 = 9
    side3 = 12
    perimeter = calculate_triangle_perimeter(side1, side2, side3)
    print(perimeter)