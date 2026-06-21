from typing import Union

def validate_positive_number(value: float, name: str) -> None:
    if value < 0:
        raise ValueError(f"{name} cannot be negative")

def calculate_area_square(side_length: float) -> float:
    validate_positive_number(side_length, "Side length")
    return side_length * side_length

def calculate_area_rectangle(length: float, width: float) -> float:
    validate_positive_number(length, "Length")
    validate_positive_number(width, "Width")
    return length * width

def calculate_area_circle(radius: float) -> float:
    import math
    validate_positive_number(radius, "Radius")
    return math.pi * radius * radius

def calculate_area_triangle(base: float, height: float) -> float:
    validate_positive_number(base, "Base")
    validate_positive_number(height, "Height")
    return 0.5 * base * height

if __name__ == '__main__':
    print(calculate_area_square(5.0))
    print(calculate_area_rectangle(4.0, 6.0))
    print(calculate_area_circle(3.0))
    print(calculate_area_triangle(7.0, 2.0))