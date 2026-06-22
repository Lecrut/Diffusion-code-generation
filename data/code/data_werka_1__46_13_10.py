def calculate_perimeter_of_triangle(side1, side2, side3):
    if not all(isinstance(side, (int, float)) and side > 0 for side in [side1, side2, side3]):
        raise ValueError("All sides must be positive numbers.")
    return side1 + side2 + side3

if __name__ == '__main__':
    valid_sides = [3, 4, 5]
    try:
        perimeter = calculate_perimeter_of_triangle(*valid_sides)
        print(perimeter)
    except ValueError as e:
        print(f"Error: {e}")

    invalid_sides_zero = [3, 4, 0]
    try:
        perimeter = calculate_perimeter_of_triangle(*invalid_sides_zero)
        print(perimeter)
    except ValueError as e:
        print(f"Error: {e}")

    invalid_sides_negative = [3, -4, 5]
    try:
        perimeter = calculate_perimeter_of_triangle(*invalid_sides_negative)
        print(perimeter)
    except ValueError as e:
        print(f"Error: {e}")