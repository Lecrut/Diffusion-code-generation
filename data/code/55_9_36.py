from typing import Union

def calculate_triangle_perimeter(side1: float, side2: float, side3: float) -> float:
    if any(side <= 0 for side in [side1, side2, side3]):
        raise ValueError("Side lengths must be positive numbers.")
    return side1 + side2 + side3

if __name__ == '__main__':
    try:
        perimeter = calculate_triangle_perimeter(3.0, 4.0, 5.0)
        print(perimeter)
    except ValueError as e:
        print(e)