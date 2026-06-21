def validate_side_lengths(side1, side2, side3):
    if not all(isinstance(side, (int, float)) for side in [side1, side2, side3]):
        raise ValueError("All sides must be numbers.")
    if any(side <= 0 for side in [side1, side2, side3]):
        raise ValueError("Side lengths must be positive numbers.")

def calculate_triangle_perimeter(side1, side2, side3):
    validate_side_lengths(side1, side2, side3)
    return side1 + side2 + side3

if __name__ == '__main__':
    try:
        side1 = 6
        side2 = 8
        side3 = 10
        perimeter = calculate_triangle_perimeter(side1, side2, side3)
        print(perimeter)
    except ValueError as e:
        print(e)