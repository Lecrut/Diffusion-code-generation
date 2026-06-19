from typing import Union

def validate_positive(value: float) -> None:
    if value <= 0:
        raise ValueError("The value must be positive.")

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

def calculate_area_triangle(base: float, height: float) -> float:
    validate_positive(base)
    validate_positive(height)
    return 0.5 * base * height

if __name__ == '__main__':
    square_side = 4.0
    rectangle_length = 5.0
    rectangle_width = 3.0
    circle_radius = 7.0
    triangle_base = 6.0
    triangle_height = 4.0
    
    print("Area of Square:", calculate_area_square(square_side))
    print("Area of Rectangle:", calculate_area_rectangle(rectangle_length, rectangle_width))
    print("Area of Circle:", calculate_area_circle(circle_radius))
    print("Area of Triangle:", calculate_area_triangle(triangle_base, triangle_height))