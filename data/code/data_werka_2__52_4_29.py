from typing import Union

class ShapeAreaCalculator:
    def calculate_area_square(self, side_length: float) -> float:
        if side_length < 0:
            raise ValueError('Side length cannot be negative')
        return side_length * side_length

    def calculate_area_rectangle(self, length: float, width: float) -> float:
        if length < 0 or width < 0:
            raise ValueError('Length and width cannot be negative')
        return length * width

    def calculate_area_circle(self, radius: float) -> float:
        import math
        if radius < 0:
            raise ValueError('Radius cannot be negative')
        return math.pi * radius * radius

if __name__ == '__main__':
    calculator = ShapeAreaCalculator()
    print("Area of Square:", calculator.calculate_area_square(5.0))
    print("Area of Rectangle:", calculator.calculate_area_rectangle(4.0, 6.0))
    print("Area of Circle:", calculator.calculate_area_circle(3.0))