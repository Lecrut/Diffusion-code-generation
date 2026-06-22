import math
from typing import List

class GeometricShape:
    def get_area(self) -> float:
        raise ValueError("Area must be implemented by subclass")

    def scale_dimensions(self, factor: float) -> None:
        if factor <= 0:
            raise ValueError("Scale factor must be strictly positive")

    def calculate_scaled_area(self, factor: float) -> float:
        self.scale_dimensions(factor)
        return self.get_area()

class Circle(GeometricShape):
    def __init__(self, radius: float) -> None:
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = radius

    def get_area(self) -> float:
        return math.pi * (self._radius ** 2)

    def scale_dimensions(self, factor: float) -> None:
        super().scale_dimensions(factor)
        self._radius *= factor

class Rectangle(GeometricShape):
    def __init__(self, width: float, height: float) -> None:
        if width < 0 or height < 0:
            raise ValueError("Dimensions cannot be negative")
        self._width = width
        self._height = height

    def get_area(self) -> float:
        return self._width * self._height

    def scale_dimensions(self, factor: float) -> None:
        super().scale_dimensions(factor)
        self._width *= factor
        self._height *= factor

class Square(GeometricShape):
    def __init__(self, side: float) -> None:
        if side < 0:
            raise ValueError("Side length cannot be negative")
        self._side = side

    def get_area(self) -> float:
        return self._side ** 2

    def scale_dimensions(self, factor: float) -> None:
        super().scale_dimensions(factor)
        self._side *= factor

if __name__ == '__main__':
    shapes: List[GeometricShape] = [
        Circle(5.0),
        Rectangle(4.0, 3.0),
        Square(2.0)
    ]

    scale_factor = 3.0

    for shape in shapes:
        original_area = shape.get_area()
        new_area = shape.calculate_scaled_area(scale_factor)
        print(f"Original: {original_area:.2f}, Scaled: {new_area:.2f}")