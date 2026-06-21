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
        perimeter = calculate_triangle_perimeter(5.0, 6.0, 7.0)
        print(perimeter)
    except ValueError as e:
        print(e)