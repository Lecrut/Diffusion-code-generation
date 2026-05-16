def calculate_perimeter(sides):
    if any(side <= 0 for side in sides):
        raise ValueError("All sides of the triangle must be positive.")
    return sum(sides)
if __name__ == '__main__':
    valid_sides = [3, 4, 5]
    try:
        perimeter = calculate_perimeter(valid_sides)
        print(perimeter)
    except ValueError as e:
        print(f"Error: {e}")
    invalid_sides_zero = [3, 4, 0]
    try:
        perimeter = calculate_perimeter(invalid_sides_zero)
        print(perimeter)
    except ValueError as e:
        print(f"Error: {e}")
    invalid_sides_negative = [3, -4, 5]
    try:
        perimeter = calculate_perimeter(invalid_sides_negative)
        print(perimeter)
    except ValueError as e:
        print(f"Error: {e}")