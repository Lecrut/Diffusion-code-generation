def validate_sides(sides):
    if not all(isinstance(side, (int, float)) for side in sides):
        raise ValueError("All sides must be numbers.")
    if any(side <= 0 for side in sides):
        raise ValueError("All sides must be positive numbers.")

def calculate_triangle_perimeter(sides):
    validate_sides(sides)
    return sum(sides)

if __name__ == '__main__':
    valid_sides = [3, 4, 5]
    try:
        perimeter = calculate_triangle_perimeter(valid_sides)
        print(perimeter)
    except ValueError as e:
        print(f"Error: {e}")

    invalid_sides_zero = [3, 4, 0]
    try:
        perimeter = calculate_triangle_perimeter(invalid_sides_zero)
        print(perimeter)
    except ValueError as e:
        print(f"Error: {e}")

    invalid_sides_negative = [3, -4, 5]
    try:
        perimeter = calculate_triangle_perimeter(invalid_sides_negative)
        print(perimeter)
    except ValueError as e:
        print(f"Error: {e}")