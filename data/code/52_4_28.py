from typing import Union

def validate_positive(value: float, name: str) -> None:
    if value < 0:
        raise ValueError(f"{name} cannot be negative")

def calculate_area_square(side_length: float) -> float:
    validate_positive(side_length, "Side length")
    return side_length * side_length

def calculate_area_rectangle(length: float, width: float) -> float:
    validate_positive(length, "Length")
    validate_positive(width, "Width")
    return length * width

def calculate_area_circle(radius: float) -> float:
    import math
    validate_positive(radius, "Radius")
    return math.pi * radius * radius

if __name__ == '__main__':
    print(calculate_area_square(5.0))
    print(calculate_area_rectangle(4.0, 6.0))
    print(calculate_area_circle(3.0))