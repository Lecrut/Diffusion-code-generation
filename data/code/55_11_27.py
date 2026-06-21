from typing import Tuple

def calculate_triangle_perimeter(side_a: float, side_b: float, side_c: float) -> float:
    return side_a + side_b + side_c

if __name__ == '__main__':
    sample_sides = (3.0, 4.0, 5.0)
    perimeter = calculate_triangle_perimeter(*sample_sides)
    print(perimeter)