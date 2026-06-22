from typing import Tuple

def calculate_triangle_perimeter(side1: float, side2: float, side3: float) -> float:
    sides = (side1, side2, side3)
    if any(side < 0 for side in sides):
        raise ValueError("Side lengths cannot be negative.")
    return sum(sides)

if __name__ == '__main__':
    try:
        triangle_sides = {
            'side_a': 5.0,
            'side_b': 6.0,
            'side_c': 7.0
        }
        perimeter = calculate_triangle_perimeter(
            triangle_sides['side_a'],
            triangle_sides['side_b'],
            triangle_sides['side_c']
        )
        print(perimeter)
    except ValueError as e:
        print(e)