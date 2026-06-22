from typing import Sequence

def validate_triangle_sides(sides: Sequence[float]) -> None:
    if len(sides) != 3:
        raise ValueError("A triangle must have exactly three sides.")
    a, b, c = sides
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("All sides must be positive numbers.")
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        raise ValueError("The sum of any two sides must be greater than the third side.")

def calculate_triangle_perimeter(side_a: float, side_b: float, side_c: float) -> float:
    validate_triangle_sides((side_a, side_b, side_c))
    return side_a + side_b + side_c

if __name__ == '__main__':
    sample_sides = [9.0, 12.0, 15.0]
    try:
        perimeter = calculate_triangle_perimeter(*sample_sides)
        print(perimeter)
    except ValueError as e:
        print(f"Error: {e}")