from typing import Union

def calculate_triangle_perimeter(side1: float, side2: float, side3: float) -> float:
    if side1 < 0 or side2 < 0 or side3 < 0:
        raise ValueError("Side lengths cannot be negative")
    return side1 + side2 + side3

if __name__ == '__main__':
    try:
        perimeter = calculate_triangle_perimeter(3.0, 4.0, 5.0)
        print(perimeter)
    except ValueError as e:
        print(e)