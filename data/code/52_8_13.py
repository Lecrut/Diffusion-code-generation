from typing import Union

class ShapeAreaCalculator:
    @staticmethod
    def calculate_square_area(side_length: float) -> float:
        return side_length * side_length

    @staticmethod
    def calculate_rectangle_area(length: float, width: float) -> float:
        return length * width

    @staticmethod
    def calculate_circle_area(radius: float) -> float:
        import math
        return math.pi * radius * radius

    @staticmethod
    def calculate_triangle_area(base: float, height: float) -> float:
        return 0.5 * base * height

if __name__ == '__main__':
    square_side = 4.0
    rectangle_length = 6.0
    rectangle_width = 4.0
    circle_radius = 3.0
    triangle_base = 5.0
    triangle_height = 3.0
    
    print("Area of Square:", ShapeAreaCalculator.calculate_square_area(square_side))
    print("Area of Rectangle:", ShapeAreaCalculator.calculate_rectangle_area(rectangle_length, rectangle_width))
    print("Area of Circle:", ShapeAreaCalculator.calculate_circle_area(circle_radius))
    print("Area of Triangle:", ShapeAreaCalculator.calculate_triangle_area(triangle_base, triangle_height))