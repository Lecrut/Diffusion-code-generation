import math
from typing import List, Union, Optional

class Shape:
    def area(self) -> float:
        raise ValueError("Base class should not be used directly")

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

class Triangle(Shape):
    def __init__(self, base: float, height: float) -> None:
        self.base = base
        self.height = height

    def area(self) -> float:
        return 0.5 * self.base * self.height

    def scale(self, factor: float) -> None:
        super().scale(factor)
        self.base *= factor
        self.height *= factor

def calculate_scaled_area(shape: Shape, factor: float) -> float:
    scaled_shape = shape.__class__(*shape.__dict__.values())
    scaled_shape.scale(factor)
    return scaled_shape.area()

if __name__ == '__main__':
    circle = Circle(5.0)
    print(calculate_scaled_area(circle, 2.0))

    rectangle = Rectangle(4.0, 6.0)
    print(calculate_scaled_area(rectangle, 1.5))

    triangle = Triangle(10.0, 8.0)
    print(calculate_scaled_area(triangle, 0.5))