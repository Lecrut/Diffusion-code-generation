def calculate_triangle_perimeter(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("All sides of the triangle must be positive numbers.")
    return a + b + c

if __name__ == '__main__':
    valid_sides = (3, 4, 5)
    try:
        perimeter = calculate_triangle_perimeter(*valid_sides)
        print(perimeter)
    except ValueError as e:
        print(f"Error: {e}")

    invalid_sides_zero = (3, 0, 5)
    try:
        perimeter = calculate_triangle_perimeter(*invalid_sides_zero)
        print(perimeter)
    except ValueError as e:
        print(f"Error: {e}")

    invalid_sides_negative = (3, -4, 5)
    try:
        perimeter = calculate_triangle_perimeter(*invalid_sides_negative)
        print(perimeter)
    except ValueError as e:
        print(f"Error: {e}")