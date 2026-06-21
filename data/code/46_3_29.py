def validate_sides(side1, side2, side3):
    if not all(isinstance(side, int) and side > 0 for side in (side1, side2, side3)):
        raise ValueError("All sides must be positive integers.")

def calculate_triangle_perimeter(side1, side2, side3):
    validate_sides(side1, side2, side3)
    return side1 + side2 + side3

if __name__ == '__main__':
    try:
        side_a = 7
        side_b = 9
        side_c = 12
        perimeter = calculate_triangle_perimeter(side_a, side_b, side_c)
        print(perimeter)
    except ValueError as e:
        print(e)