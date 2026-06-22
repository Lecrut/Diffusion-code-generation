def is_valid_triangle_side(side):
    return isinstance(side, (int, float)) and side > 0

def calculate_triangle_perimeter(side1, side2, side3):
    if not all(is_valid_triangle_side(side) for side in [side1, side2, side3]):
        raise ValueError("Side lengths must be positive numbers.")
    return side1 + side2 + side3

if __name__ == '__main__':
    try:
        side_a = 6
        side_b = 8
        side_c = 10
        perimeter = calculate_triangle_perimeter(side_a, side_b, side_c)
        print(perimeter)
    except ValueError as e:
        print(e)