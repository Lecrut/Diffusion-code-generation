from typing import Union

def calculate_triangle_perimeter(side1: float, side2: float, side3: float) -> float:
    if any(side < 0 for side in (side1, side2, side3)):
        raise ValueError("Side lengths cannot be negative.")
    return sum((side1, side2, side3))

if __name__ == '__main__':
    try:
        triangle_perimeter = calculate_triangle_perimeter(7.5, 9.2, 6.8)
        print(triangle_perimeter)
    except ValueError as e:
        print(e)