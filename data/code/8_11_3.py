import math
from typing import List, Union

class Shape:
    def area(self) -> float:
        return 0.0

    def scale(self, factor: float) -> None:
        if factor <= 0:
            raise ValueError("Scale factor must be positive")

    def scaled_area(self, factor: float) -> float:
        original_area = self.area()
        self.scale(factor)
        new_area = self.area()
        self.scale(1.0 / factor)
        return original_area * (factor ** 2)

class Circle(Shape):
    def __init__(self, radius: float) -> None:
        if radius < 0:
            raise ValueError("Radius must be non-negative")
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def scale(self, factor: float) -> None:
        super().scale(factor)
        self.radius *= factor

class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        if width < 0 or height < 0:
            raise ValueError("Dimensions must be non-negative")
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
        if base < 0 or height < 0:
            raise ValueError("Dimensions must be non-negative")
        self.base = base
        self.height = height

    def area(self) -> float:
        return 0.5 * self.base * self.height

    def scale(self, factor: float) -> None:
        super().scale(factor)
        self.base *= factor
        self.height *= factor

def calculate_total_area(shapes: List[Shape]) -> float:
    total = 0.0
    for shape in shapes:
        total += shape.area()
    return total

def scale_all_shapes(shapes: List[Shape], factor: float) -> None:
    for shape in shapes:
        shape.scale(factor)

if __name__ == '__main__':
    circle = Circle(5.0)
    rectangle = Rectangle(4.0, 6.0)
    triangle = Triangle(3.0, 8.0)

    shapes = [circle, rectangle, triangle]

    print(calculate_total_area(shapes))

    for shape in shapes:
        print(shape.scaled_area(2.0))

    scale_all_shapes(shapes, 3.0)
    print(calculate_total_area(shapes))