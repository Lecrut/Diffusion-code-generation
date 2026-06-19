def calculate_triangle_perimeter(side1, side2, side3):
    if not all(isinstance(side, (int, float)) for side in [side1, side2, side3]):
        raise ValueError("All sides must be numbers.")
    if any(side <= 0 for side in [side1, side2, side3]):
        raise ValueError("All sides must be positive numbers.")
    return side1 + side2 + side3

if __name__ == '__main__':
    try:
        perimeter = calculate_triangle_perimeter(3, 4, 5)
        print(perimeter)
    except ValueError as e:
        print(e)