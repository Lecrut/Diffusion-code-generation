def calculate_perimeter(side1, side2, side3):
    if not (side1 > 0 and side2 > 0 and side3 > 0):
        raise ValueError("All sides must be positive numbers.")
    if not (side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1):
        raise ValueError("The given sides do not form a valid triangle.")
    return side1 + side2 + side3

if __name__ == '__main__':
    side1 = 9
    side2 = 12
    side3 = 15
    perimeter = calculate_perimeter(side1, side2, side3)
    print(perimeter)