from typing import Union

class ShapeAreaCalculator:
    PI = 3.141592653589793

    @staticmethod
    def calculate_area_square(side_length: float) -> float:
        return side_length * side_length

    @staticmethod
    def calculate_area_rectangle(length: float, width: float) -> float:
        return length * width

    @staticmethod
    def calculate_area_circle(radius: float) -> float:
        return ShapeAreaCalculator.PI * radius * radius

    @staticmethod
    def calculate_area_triangle(base: float, height: float) -> float:
        return 0.5 * base * height

if __name__ == '__main__':
    square_side = 4.0
    rectangle_length = 5.0
    rectangle_width = 3.0
    circle_radius = 7.0
    triangle_base = 6.0
    triangle_height = 4.0

    print("Area of Square:", ShapeAreaCalculator.calculate_area_square(square_side))
    print("Area of Rectangle:", ShapeAreaCalculator.calculate_area_rectangle(rectangle_length, rectangle_width))
    print("Area of Circle:", ShapeAreaCalculator.calculate_area_circle(circle_radius))
    print("Area of Triangle:", ShapeAreaCalculator.calculate_area_triangle(triangle_base, triangle_height))