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
    rectangle_length = 5.0
    rectangle_width = 3.0
    circle_radius = 7.0
    triangle_base = 6.0
    triangle_height = 8.0

    print(f"Area of square: {calculate_area_square(square_side)}")
    print(f"Area of rectangle: {calculate_area_rectangle(rectangle_length, rectangle_width)}")
    print(f"Area of circle: {calculate_area_circle(circle_radius)}")
    print(f"Area of triangle: {calculate_area_triangle(triangle_base, triangle_height)}")