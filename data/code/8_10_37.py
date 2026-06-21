from typing import Union

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
    print(f"Original Circle Area: {circle.area}")
    circle.scale_area(2.0)
    print(f"Scaled Circle Area: {circle.area}")

    rectangle = Rectangle(width=4.0, height=6.0)
    print(f"Original Rectangle Area: {rectangle.area}")
    rectangle.scale_area(1.5)
    print(f"Scaled Rectangle Area: {rectangle.area}")