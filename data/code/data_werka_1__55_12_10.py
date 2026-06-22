from typing import Tuple
MIN_SIDE_LENGTH: float = 0.0

def is_valid_triangle(side_a: float, side_b: float, side_c: float) -> bool:
    return side_a > MIN_SIDE_LENGTH and side_b > MIN_SIDE_LENGTH and (side_c > MIN_SIDE_LENGTH) and (side_a + side_b > side_c) and (side_a + side_c > side_b) and (side_b + side_c > side_a)

def calculate_triangle_perimeter(side_a: float, side_b: float, side_c: float) -> float:
    if not is_valid_triangle(side_a, side_b, side_c):
        raise ValueError('Invalid triangle sides provided.')
    return side_a + side_b + side_c
if __name__ == '__main__':
    sample_sides: Tuple[float, float, float] = (3.0, 4.0, 5.0)
    try:
        perimeter: float = calculate_triangle_perimeter(*sample_sides)
        print(perimeter)
    except ValueError as e:
        print(e)