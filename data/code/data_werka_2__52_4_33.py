from typing import Union

def calculate_area_square(side_length: float) -> float:
    if side_length < 0:
        raise ValueError('Side length cannot be negative')
    return side_length * side_length

def calculate_area_rectangle(length: float, width: float) -> float:
    if length < 0 or width < 0:
        raise ValueError('Length and width cannot be negative')
    return length * width

def calculate_area_circle(radius: float) -> float:
    import math
    if radius < 0:
        raise ValueError('Radius cannot be negative')
    return math.pi * radius * radius

def calculate_area_triangle(base: float, height: float) -> float:
    if base < 0 or height < 0:
        raise ValueError('Base and height cannot be negative')
    return 0.5 * base * height

if __name__ == '__main__':
    square_side = 4.0
    rectangle_length = 5.0
    rectangle_width = 3.0
    circle_radius = 7.0
    triangle_base = 6.0
    triangle_height = 8.0
    
    print(f"Area of Square: {calculate_area_square(square_side)}")
    print(f"Area of Rectangle: {calculate_area_rectangle(rectangle_length, rectangle_width)}")
    print(f"Area of Circle: {calculate_area_circle(circle_radius):.2f}")
    print(f"Area of Triangle: {calculate_area_triangle(triangle_base, triangle_height)}")