from typing import NamedTuple

class TriangleSides(NamedTuple):
    side_a: float
    side_b: float
    side_c: float

def calculate_triangle_perimeter(sides: TriangleSides) -> float:
    a, b, c = sides
    if any(side <= 0 for side in sides):
        raise ValueError("All sides must be positive numbers.")
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        raise ValueError("The sum of any two sides must be greater than the third side.")
    return a + b + c

if __name__ == '__main__':
    sample_sides = TriangleSides(9.0, 12.0, 15.0)
    try:
        perimeter = calculate_triangle_perimeter(sample_sides)
        print(perimeter)
    except ValueError as e:
        print(f"Error: {e}")