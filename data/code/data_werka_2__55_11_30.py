from typing import Tuple

def calculate_triangle_perimeter(side_a: float, side_b: float, side_c: float) -> float:
    perimeter = side_a + side_b + side_c
    return perimeter

if __name__ == '__main__':
    sample_sides: Tuple[float, float, float] = (9.0, 12.0, 15.0)
    calculated_perimeter: float = calculate_triangle_perimeter(*sample_sides)
    print(calculated_perimeter)