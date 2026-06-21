from typing import Tuple

def is_valid_triangle(side_a: float, side_b: float, side_c: float) -> bool:
    if side_a <= 0 or side_b <= 0 or side_c <= 0:
        return False
    if (side_a + side_b <= side_c) or (side_a + side_c <= side_b) or (side_b + side_c <= side_a):
        return False
    return True

def calculate_triangle_perimeter(side_a: float, side_b: float, side_c: float) -> float:
    if not is_valid_triangle(side_a, side_b, side_c):
        raise ValueError("Invalid triangle sides provided.")
    return side_a + side_b + side_c

if __name__ == '__main__':
    sample_sides: Tuple[float, float, float] = (9.0, 12.0, 15.0)
    try:
        perimeter: float = calculate_triangle_perimeter(*sample_sides)
        print(perimeter)
    except ValueError as e:
        print(f"Error: {e}")