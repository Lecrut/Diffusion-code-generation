from typing import NamedTuple

class TriangleSides(NamedTuple):
    side_a: float
    side_b: float
    side_c: float

def calculate_triangle_perimeter(sides: TriangleSides) -> float:
    return sides.side_a + sides.side_b + sides.side_c

if __name__ == '__main__':
    sample_sides = TriangleSides(3.0, 4.0, 5.0)
    perimeter = calculate_triangle_perimeter(sample_sides)
    print(perimeter)