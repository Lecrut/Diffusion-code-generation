import math
from typing import List

class Shape:
    def area(self) -> float:
        raise ValueError("Base class should not be used directly")

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
        self._radius = radius

    def area(self) -> float:
        return math.pi * self._radius ** 2

    def scale(self, factor: float) -> None:
        super().scale(factor)
        self._radius *= factor

class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        if width < 0 or height < 0:
            raise ValueError("Dimensions must be non-negative")
        self._width = width
        self._height = height

    def area(self) -> float:
        return self._width * self._height

    def scale(self, factor: float) -> None:
        super().scale(factor)
        self._width *= factor
        self._height *= factor

if __name__ == '__main__':
    circle = Circle(5.0)
    print(circle.scaled_area(2.0))
    
    rect = Rectangle(4.0, 6.0)
    print(rect.scaled_area(3.0))