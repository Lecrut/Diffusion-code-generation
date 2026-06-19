def calculate_triangle_perimeter(side1, side2, side3):
    sides = [side1, side2, side3]
    if any(side <= 0 for side in sides):
        raise ValueError("All sides of the triangle must be positive numbers.")
    return sum(sides)

if __name__ == '__main__':
    try:
        valid_triangle_sides = [7, 10, 5]
        perimeter = calculate_triangle_perimeter(*valid_triangle_sides)
        print(perimeter)
    except ValueError as e:
        print(f"Error: {e}")

    try:
        invalid_triangle_sides_zero = [7, 0, 5]
        perimeter = calculate_triangle_perimeter(*invalid_triangle_sides_zero)
        print(perimeter)
    except ValueError as e:
        print(f"Error: {e}")

    try:
        invalid_triangle_sides_negative = [7, -10, 5]
        perimeter = calculate_triangle_perimeter(*invalid_triangle_sides_negative)
        print(perimeter)
    except ValueError as e:
        print(f"Error: {e}")