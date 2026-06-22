def calculate_triangle_perimeter(side1: float, side2: float, side3: float) -> float:
    MIN_SIDE_LENGTH = 0.0
    if side1 <= MIN_SIDE_LENGTH or side2 <= MIN_SIDE_LENGTH or side3 <= MIN_SIDE_LENGTH:
        raise ValueError("All sides must be greater than zero.")
    return side1 + side2 + side3

if __name__ == '__main__':
    side_a = 7.5
    side_b = 8.5
    side_c = 9.5
    try:
        perimeter = calculate_triangle_perimeter(side_a, side_b, side_c)
        print(perimeter)
    except ValueError as e:
        print(e)