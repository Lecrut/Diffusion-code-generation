def validate_side_length(side):
    if side <= 0:
        raise ValueError("All sides of the triangle must be positive numbers.")

def calculate_triangle_perimeter(side1, side2, side3):
    validate_side_length(side1)
    validate_side_length(side2)
    validate_side_length(side3)
    return side1 + side2 + side3

if __name__ == '__main__':
    valid_sides = [3, 4, 5]
    try:
        perimeter = calculate_triangle_perimeter(*valid_sides)
        print(perimeter)
    except ValueError as e:
        print(f"Error: {e}")

    invalid_sides_zero = [3, 4, 0]
    try:
        perimeter = calculate_triangle_perimeter(*invalid_sides_zero)
        print(perimeter)
    except ValueError as e:
        print(f"Error: {e}")

    invalid_sides_negative = [3, -4, 5]
    try:
        perimeter = calculate_triangle_perimeter(*invalid_sides_negative)
        print(perimeter)
    except ValueError as e:
        print(f"Error: {e}")