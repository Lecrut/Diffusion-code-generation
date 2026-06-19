from typing import Tuple
TRIANGLE_SIDES_COUNT = 3

def compute_triangle_perimeter(sides: Tuple[float, float, float]) -> float:
    if len(sides) != TRIANGLE_SIDES_COUNT:
        raise ValueError('Exactly three sides are required to form a triangle.')
    perimeter = sum(sides)
    return perimeter
if __name__ == '__main__':
    sample_sides: Tuple[float, float, float] = (6.0, 8.0, 10.0)
    try:
        perimeter: float = compute_triangle_perimeter(sample_sides)
        print(perimeter)
    except ValueError as e:
        print(e)