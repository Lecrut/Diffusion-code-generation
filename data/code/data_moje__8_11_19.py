import math
from typing import List, Union, Optional

SHAPE_ERROR_MSG = "Base class should not be used directly"

class Shape:
    def area(self) -> float:
        raise ValueError(SHAPE_ERROR_MSG)

    def scale(self, factor: float) -> None:
        if factor <= 0:
            raise ValueError("Scale factor must be positive")

class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def scale(self, factor: float) -> None:
        super().scale(factor)
        self.radius *= factor

class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def scale(self, factor: float) -> None:
        super().scale(factor)
        self.width *= factor
        self.height *= factor

def calculate_scaled_area(shape: Shape, factor: float) -> float:
    original_area = shape.area()
    shape.scale(factor)
    new_area = shape.area()
    shape.scale(1.0 / factor)
    return new_area

if __name__ == '__main__':
    circle = Circle(5.0)
    rectangle = Rectangle(4.0, 6.0)

    factor = 2.0

    circle_scaled_area = calculate_scaled_area(circle, factor)
    print(circle_scaled_area)

    rectangle_scaled_area = calculate_scaled_area(rectangle, factor)
    print(rectangle_scaled_area)