from typing import Union

def validate_side_length(side: float) -> None:
    if side < 0:
        raise ValueError("Side lengths cannot be negative.")

def calculate_triangle_perimeter(side1: float, side2: float, side3: float) -> float:
    validate_side_length(side1)
    validate_side_length(side2)
    validate_side_length(side3)
    return side1 + side2 + side3

if __name__ == '__main__':
    try:
        side_a = 5.0
        side_b = 6.0
        side_c = 7.0
        triangle_perimeter = calculate_triangle_perimeter(side_a, side_b, side_c)
        print(triangle_perimeter)
    except ValueError as e:
        print(e)