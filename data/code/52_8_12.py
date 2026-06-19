from typing import Union

def calculate_area_square(side_length: float) -> float:
    return side_length * side_length

def calculate_area_rectangle(length: float, width: float) -> float:
    return length * width

def calculate_area_circle(radius: float) -> float:
    import math
    return math.pi * radius * radius

def calculate_area_triangle(base: float, height: float) -> float:
    return 0.5 * base * height

if __name__ == '__main__':
    square_side = 3.0
    rectangle_length = 8.0
    rectangle_width = 2.0
    circle_radius = 5.0
    triangle_base = 7.0
    triangle_height = 2.0
    
    square_area = calculate_area_square(square_side)
    rectangle_area = calculate_area_rectangle(rectangle_length, rectangle_width)
    circle_area = calculate_area_circle(circle_radius)
    triangle_area = calculate_area_triangle(triangle_base, triangle_height)
    
    print(f"Area of Square: {square_area}")
    print(f"Area of Rectangle: {rectangle_area}")
    print(f"Area of Circle: {circle_area:.2f}")
    print(f"Area of Triangle: {triangle_area}")