from typing import Dict

def calculate_triangle_perimeter(side1: float, side2: float, side3: float) -> float:
    if any(side < 0 for side in (side1, side2, side3)):
        raise ValueError("Side lengths cannot be negative.")
    return sum((side1, side2, side3))

if __name__ == '__main__':
    try:
        sides = {
            'side_a': 5.0,
            'side_b': 6.0,
            'side_c': 7.0
        }
        triangle_perimeter = calculate_triangle_perimeter(sides['side_a'], sides['side_b'], sides['side_c'])
        print(triangle_perimeter)
    except ValueError as e:
        print(e)