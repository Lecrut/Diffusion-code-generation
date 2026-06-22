def is_valid_side_length(side):
    return side > 0

def validate_triangle_sides(sides):
    if not all(is_valid_side_length(side) for side in sides):
        raise ValueError("All sides of the triangle must be positive numbers.")

def calculate_triangle_perimeter(side1, side2, side3):
    sides = [side1, side2, side3]
    validate_triangle_sides(sides)
    return sum(sides)

if __name__ == '__main__':
    try:
        perimeter = calculate_triangle_perimeter(3, 4, 5)
        print(perimeter)
    except ValueError as e:
        print(e)

    invalid_sides_zero = [3, 4, 0]
    try:
        perimeter = calculate_triangle_perimeter(*invalid_sides_zero)
        print(perimeter)
    except ValueError as e:
        print(e)

    invalid_sides_negative = [3, -4, 5]
    try:
        perimeter = calculate_triangle_perimeter(*invalid_sides_negative)
        print(perimeter)
    except ValueError as e:
        print(e)