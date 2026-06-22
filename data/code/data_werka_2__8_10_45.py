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
        super().__init__(Circle.PI * radius ** 2)

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        super().__init__(width * height)

if __name__ == '__main__':
    circle = Circle(radius=5)
    print(circle.get_area())
    circle.scale_area(2.0)
    print(circle.get_area())

    rectangle = Rectangle(width=5.0, height=3.0)
    print(rectangle.get_area())
    rectangle.scale_area(1.5)
    print(rectangle.get_area())