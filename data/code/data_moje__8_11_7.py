import math
from typing import Union

class Shape:
    def get_area(self) -> float:
        raise ValueError("Must override get_area in subclass")

    def scale(self, factor: float) -> None:
        if factor <= 0:
            raise ValueError("Scale factor must be positive")

class Circle(Shape):
    def __init__(self, radius: float) -> None:
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def get_area(self) -> float:
        return math.pi * (self.radius ** 2)

    def scale(self, factor: float) -> None:
        super().scale(factor)
        self.radius *= factor

class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        if width < 0 or height < 0:
            raise ValueError("Dimensions cannot be negative")
        self.width = width
        self.height = height

    def get_area(self) -> float:
        return self.width * self.height

    def scale(self, factor: float) -> None:
        super().scale(factor)
        self.width *= factor
        self.height *= factor

class Triangle(Shape):
    def __init__(self, base: float, height: float) -> None:
        if base < 0 or height < 0:
            raise ValueError("Dimensions cannot be negative")
        self.base = base
        self.height = height

    def get_area(self) -> float:
        return 0.5 * self.base * self.height

    def scale(self, factor: float) -> None:
        super().scale(factor)
        self.base *= factor
        self.height *= factor

def calculate_scheduled_scaling_area(shape: Shape, factor: float) -> float:
    original_area = shape.get_area()
    shape.scale(factor)
    new_area = shape.get_area()
    shape.scale(1.0 / factor)
    return new_area

if __name__ == '__main__':
    circle = Circle(5.0)
    rect = Rectangle(4.0, 6.0)
    tri = Triangle(10.0, 8.0)

    scale_factor = 2.5

    print(calculate_scheduled_scaling_area(circle, scale_factor))
    print(calculate_scheduled_scaling_area(rect, scale_factor))
    print(calculate_scheduled_scaling_area(tri, scale_factor))