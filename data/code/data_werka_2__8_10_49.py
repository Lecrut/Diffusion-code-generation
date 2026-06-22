from typing import Union

class Shape:
    def __init__(self, area: float):
        self._validate_area(area)
        self._area = area

    @staticmethod
    def _validate_area(area: float) -> None:
        if area < 0:
            raise ValueError("Area must be non-negative")

    def scale_area(self, factor: float) -> None:
        self._validate_scale_factor(factor)
        self._area *= factor

    @staticmethod
    def _validate_scale_factor(factor: float) -> None:
        if factor <= 0:
            raise ValueError("Scale factor must be positive")

    def get_area(self) -> float:
        return self._area

class Circle(Shape):
    PI = 3.14159

    def __init__(self, radius: float):
        area = self.PI * radius ** 2
        super().__init__(area)

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        area = width * height
        super().__init__(area)

if __name__ == '__main__':
    circle = Circle(radius=5)
    print(f"Original Circle Area: {circle.get_area()}")
    circle.scale_area(2.0)
    print(f"Scaled Circle Area: {circle.get_area()}")

    rectangle = Rectangle(width=4.0, height=6.0)
    print(f"Original Rectangle Area: {rectangle.get_area()}")
    rectangle.scale_area(1.5)
    print(f"Scaled Rectangle Area: {rectangle.get_area()}")