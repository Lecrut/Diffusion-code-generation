def calculate_triangle_perimeter(side1, side2, side3):
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        raise ValueError("Side lengths must be positive numbers.")
    return side1 + side2 + side3

if __name__ == '__main__':
    side1 = 5
    side2 = 6
    side3 = 7
    perimeter = calculate_triangle_perimeter(side1, side2, side3)
    print(perimeter)