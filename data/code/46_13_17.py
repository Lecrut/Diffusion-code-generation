def calculate_triangle_perimeter(sides):
    if len(sides) != 3:
        raise ValueError("Exactly three sides are required to form a triangle.")
    if any(side <= 0 for side in sides):
        raise ValueError("All sides of the triangle must be positive numbers.")
    return sum(sides)

if __name__ == '__main__':
    valid_sides = [6, 8, 10]
    try:
        perimeter = calculate_triangle_perimeter(valid_sides)
        print(perimeter)
    except ValueError as e:
        print(f"Error: {e}")

    invalid_sides_zero = [6, 8, 0]
    try:
        perimeter = calculate_triangle_perimeter(invalid_sides_zero)
        print(perimeter)
    except ValueError as e:
        print(f"Error: {e}")

    invalid_sides_negative = [6, -8, 10]
    try:
        perimeter = calculate_triangle_perimeter(invalid_sides_negative)
        print(perimeter)
    except ValueError as e:
        print(f"Error: {e}")