from typing import Union

def calculate_triangle_perimeter(side1: float, side2: float, side3: float) -> float:
    if side1 < 0 or side2 < 0 or side3 < 0:
        raise ValueError("Side lengths cannot be negative.")
    perimeter = side1 + side2 + side3
    return perimeter

if __name__ == '__main__':
    try:
        side_a = 6.0
        side_b = 8.0
        side_c = 10.0
        triangle_perimeter = calculate_triangle_perimeter(side_a, side_b, side_c)
        print(triangle_perimeter)
    except ValueError as e:
        print(e)