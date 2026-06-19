from typing import Tuple

def is_valid_triangle(side_a: float, side_b: float, side_c: float) -> bool:
    return (side_a > 0 and side_b > 0 and side_c > 0) and \
           (side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a)

def calculate_triangle_perimeter(side_a: float, side_b: float, side_c: float) -> float:
    if not is_valid_triangle(side_a, side_b, side_c):
        raise ValueError("Invalid triangle sides")
    return side_a + side_b + side_c

if __name__ == '__main__':
    sample_sides: Tuple[float, float, float] = (6.0, 8.0, 10.0)
    try:
        perimeter: float = calculate_triangle_perimeter(*sample_sides)
        print(perimeter)
    except ValueError as e:
        print(e)