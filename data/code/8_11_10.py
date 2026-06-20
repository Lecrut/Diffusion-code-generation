import math
from typing import List, Tuple

class Shape:
    def __init__(self) -> None:
        self._sides: List[float] = []

    def area(self) -> float:
        return 0.0

    def scale_dimensions(self, factor: float) -> None:
        if factor <= 0:
            raise ValueError("Scale factor must be positive")
        self._sides = [s * factor for s in self._sides]

    def scaled_area(self, factor: float) -> float:
        self.scale_dimensions(factor)
        return self.area()

class Circle(Shape):
    def __init__(self, radius: float) -> None:
        super().__init__()
        self._radius = radius
        self._sides = [radius]

    def area(self) -> float:
        return math.pi * (self._radius ** 2)

    def scale_dimensions(self, factor: float) -> None:
        super().scale_dimensions(factor)
        self._radius = self._sides[0]

class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        super().__init__()
        self._width = width
        self._height = height
        self._sides = [width, height]

    def area(self) -> float:
        return self._width * self._height

    def scale_dimensions(self, factor: float) -> None:
        super().scale_dimensions(factor)
        self._width = self._sides[0]
        self._height = self._sides[1]

class Triangle(Shape):
    def __init__(self, base: float, height: float) -> None:
        super().__init__()
        self._base = base
        self._height = height
        self._sides = [base, height]

    def area(self) -> float:
        return 0.5 * self._base * self._height

    def scale_dimensions(self, factor: float) -> None:
        super().scale_dimensions(factor)
        self._base = self._sides[0]
        self._height = self._sides[1]

def run_demo() -> None:
    circle = Circle(5.0)
    rect = Rectangle(4.0, 6.0)
    triangle = Triangle(10.0, 5.0)

    print(f"Initial Circle Area: {circle.area():.4f}")
    print(f"Initial Rectangle Area: {rect.area():.4f}")
    print(f"Initial Triangle Area: {triangle.area():.4f}")

    print(f"Circle Scaled Area (2x): {circle.scaled_area(2.0):.4f}")
    print(f"Rectangle Scaled Area (0.5x): {rect.scaled_area(0.5):.4f}")
    print(f"Triangle Scaled Area (3x): {triangle.scaled_area(3.0):.4f}")

if __name__ == '__main__':
    run_demo()