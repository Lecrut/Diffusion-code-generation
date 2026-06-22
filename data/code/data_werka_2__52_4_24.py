from typing import Union

def validate_positive(value: float) -> None:
    if value < 0:
        raise ValueError('Value cannot be negative')

def calculate_area_square(side_length: float) -> float:
    validate_positive(side_length)
    return side_length * side_length

def calculate_area_rectangle(length: float, width: float) -> float:
    validate_positive(length)
    validate_positive(width)
    return length * width

def calculate_area_circle(radius: float) -> float:
    import math
    validate_positive(radius)
    return math.pi * radius * radius

if __name__ == '__main__':
    print(calculate_area_square(5.0))
    print(calculate_area_rectangle(4.0, 6.0))
    print(f"Circle Area: {calculate_area_circle(3.0):.2f}")