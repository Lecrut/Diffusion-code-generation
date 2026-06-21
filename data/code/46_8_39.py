def validate_sides(side1, side2, side3):
    if not all(isinstance(x, (int, float)) for x in [side1, side2, side3]):
        raise ValueError("All sides must be numbers.")
    if any(x <= 0 for x in [side1, side2, side3]):
        raise ValueError("All sides must be positive numbers.")

def calculate_triangle_perimeter(side1, side2, side3):
    validate_sides(side1, side2, side3)
    return side1 + side2 + side3

if __name__ == '__main__':
    sample_side1 = 7
    sample_side2 = 8
    sample_side3 = 9
    perimeter = calculate_triangle_perimeter(sample_side1, sample_side2, sample_side3)
    print(perimeter)