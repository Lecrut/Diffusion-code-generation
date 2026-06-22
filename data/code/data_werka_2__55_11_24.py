from typing import Tuple

def validate_triangle_sides(side_a: float, side_b: float, side_c: float) -> None:
    if side_a <= 0 or side_b <= 0 or side_c <= 0:
        raise ValueError("All sides must be positive numbers.")
    if (side_a + side_b <= side_c) or (side_a + side_c <= side_b) or (side_b + side_c <= side_a):
        raise ValueError("The sum of any two sides must be greater than the third side.")

def calculate_triangle_perimeter(side_a: float, side_b: float, side_c: float) -> float:
    validate_triangle_sides(side_a, side_b, side_c)
    return side_a + side_b + side_c

if __name__ == '__main__':
    sample_sides: Tuple[float, float, float] = (9.0, 12.0, 15.0)
    try:
        perimeter: float = calculate_triangle_perimeter(*sample_sides)
        print(perimeter)
    except ValueError as e:
        print(f"Error: {e}")