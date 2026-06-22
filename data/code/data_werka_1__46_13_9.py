def calculate_triangle_perimeter(side1, side2, side3):
    sides = [side1, side2, side3]
    if any(side <= 0 for side in sides):
        raise ValueError("All sides of the triangle must be positive.")
    return sum(sides)

if __name__ == '__main__':
    valid_sides = {'a': 3, 'b': 4, 'c': 5}
    try:
        perimeter = calculate_triangle_perimeter(valid_sides['a'], valid_sides['b'], valid_sides['c'])
        print(perimeter)
    except ValueError as e:
        print(f"Error: {e}")

    invalid_sides_zero = {'a': 3, 'b': 4, 'c': 0}
    try:
        perimeter = calculate_triangle_perimeter(invalid_sides_zero['a'], invalid_sides_zero['b'], invalid_sides_zero['c'])
        print(perimeter)
    except ValueError as e:
        print(f"Error: {e}")

    invalid_sides_negative = {'a': 3, 'b': -4, 'c': 5}
    try:
        perimeter = calculate_triangle_perimeter(invalid_sides_negative['a'], invalid_sides_negative['b'], invalid_sides_negative['c'])
        print(perimeter)
    except ValueError as e:
        print(f"Error: {e}")