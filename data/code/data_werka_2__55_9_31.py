from typing import Union

def calculate_triangle_perimeter(side1: float, side2: float, side3: float) -> float:
    if side1 < 0 or side2 < 0 or side3 < 0:
        raise ValueError("Side lengths cannot be negative.")
    return side1 + side2 + side3

if __name__ == '__main__':
    try:
        sides = {
            'side_a': 5.0,
            'side_b': 6.0,
            'side_c': 7.0
        }
        perimeter = calculate_triangle_perimeter(sides['side_a'], sides['side_b'], sides['side_c'])
        print(perimeter)
    except ValueError as e:
        print(e)