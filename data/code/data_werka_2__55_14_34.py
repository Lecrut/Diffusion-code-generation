def calculate_triangle_perimeter(side1, side2, side3):
    MIN_SIDE_LENGTH = 0
    if not all(isinstance(s, (int, float)) for s in [side1, side2, side3]):
        raise ValueError("All sides must be numbers")
    if any(s <= MIN_SIDE_LENGTH for s in [side1, side2, side3]):
        raise ValueError("All sides must be positive numbers")
    return side1 + side2 + side3

if __name__ == '__main__':
    side1 = 7
    side2 = 10
    side3 = 5
    perimeter = calculate_triangle_perimeter(side1, side2, side3)
    print(perimeter)