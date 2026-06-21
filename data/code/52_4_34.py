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
    square_side = 5.0
    rectangle_length = 4.0
    rectangle_width = 6.0
    circle_radius = 3.0
    
    print(f"Area of Square: {calculate_area_square(square_side)}")
    print(f"Area of Rectangle: {calculate_area_rectangle(rectangle_length, rectangle_width)}")
    print(f"Area of Circle: {calculate_area_circle(circle_radius):.2f}")