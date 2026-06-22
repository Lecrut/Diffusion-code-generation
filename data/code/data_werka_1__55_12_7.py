from typing import Tuple

def validate_sides(a: float, b: float, c: float) -> None:
    if not (a > 0 and b > 0 and c > 0):
        raise ValueError("All sides must be positive numbers.")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("The sum of any two sides must be greater than the third side.")

def calculate_triangle_perimeter(side_a: float, side_b: float, side_c: float) -> float:
    validate_sides(side_a, side_b, side_c)
    return side_a + side_b + side_c

if __name__ == '__main__':
    sample_sides: Tuple[float, float, float] = (6.0, 8.0, 10.0)
    try:
        perimeter: float = calculate_triangle_perimeter(*sample_sides)
        print(perimeter)
    except ValueError as e:
        print(e)