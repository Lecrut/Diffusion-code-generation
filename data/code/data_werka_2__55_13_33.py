def is_valid_side(side):
    return isinstance(side, (int, float)) and side > 0

def calculate_triangle_perimeter(a, b, c):
    if not all(is_valid_side(side) for side in [a, b, c]):
        raise ValueError("All sides must be positive numeric types.")
    return a + b + c

if __name__ == '__main__':
    try:
        side1 = 6
        side2 = 8
        side3 = 10
        perimeter = calculate_triangle_perimeter(side1, side2, side3)
        print(perimeter)
    except ValueError as e:
        print(e)