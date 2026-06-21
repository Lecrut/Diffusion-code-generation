from typing import TypeVar

T = TypeVar('T', bound='Shape')

class Shape:
    def __init__(self, area: float):
        if area < 0:
            raise ValueError("Area must be non-negative")
        self._area = area

    @property
    def area(self) -> float:
        return self._area

    def scale_area(self, factor: float) -> None:
        if factor <= 0:
            raise ValueError("Scale factor must be positive")
        self._area *= factor

class Circle(Shape):
    PI = 3.14159
    def __init__(self, radius: float):
        super().__init__(Circle.PI * radius ** 2)

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        super().__init__(width * height)

if __name__ == '__main__':
    circle = Circle(radius=5.0)
    rectangle = Rectangle(width=3.0, height=4.0)

    print("Original Circle Area:", circle.area)
    circle.scale_area(2.0)
    print("Scaled Circle Area:", circle.area)

    print("Original Rectangle Area:", rectangle.area)
    rectangle.scale_area(1.5)
    print("Scaled Rectangle Area:", rectangle.area)