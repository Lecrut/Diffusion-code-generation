from typing import Union

def calculate_area_square(side_length: float) -> float:
    return side_length ** 2

def calculate_area_rectangle(length: float, width: float) -> float:
    return length * width

def calculate_area_circle(radius: float) -> float:
    import math
    return math.pi * radius ** 2

def calculate_area_triangle(base: float, height: float) -> float:
    return 0.5 * base * height

if __name__ == '__main__':
    square_side = 4.0
    rectangle_length = 6.0
    rectangle_width = 4.0
    circle_radius = 3.0
    triangle_base = 5.0
    triangle_height = 3.0

    print("Area of Square:", calculate_area_square(square_side))
    print("Area of Rectangle:", calculate_area_rectangle(rectangle_length, rectangle_width))
    print("Area of Circle:", calculate_area_circle(circle_radius))
    print("Area of Triangle:", calculate_area_triangle(triangle_base, triangle_height))