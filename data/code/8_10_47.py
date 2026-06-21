from typing import Union

class Shape:
    def __init__(self, area: float):
        self._validate_area(area)
        self._area = area

    @property
    def area(self) -> float:
        return self._area

    def scale_area(self, factor: float) -> None:
        if factor <= 0:
            raise ValueError("Scale factor must be positive")
        self._area *= factor

    def get_area(self) -> float:
        return self.area

    def _validate_area(self, area: float) -> None:
        if area < 0:
            raise ValueError("Area must be non-negative")

class Circle(Shape):
    PI = 3.14159

    def __init__(self, radius: float):
        super().__init__(Circle.PI * radius ** 2)

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        super().__init__(width * height)

if __name__ == '__main__':
    circle = Circle(radius=5)
    print(f"Original Circle Area: {circle.get_area()}")
    circle.scale_area(factor=2)
    print(f"Scaled Circle Area: {circle.get_area()}")

    rectangle = Rectangle(width=4.0, height=6.0)
    print(f"Original Rectangle Area: {rectangle.get_area()}")
    rectangle.scale_area(factor=1.5)
    print(f"Scaled Rectangle Area: {rectangle.get_area()}")