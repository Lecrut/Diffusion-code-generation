from math import pi
from typing import Union

Shape = Union['Circle', 'Square', 'Rectangle']

class Circle:
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return pi * self.radius ** 2

    def scale(self, factor: float) -> 'Circle':
        self.radius *= factor
        return self

class Square:
    def __init__(self, side: float) -> None:
        self.side = side

    def area(self) -> float:
        return self.side ** 2

    def scale(self, factor: float) -> 'Square':
        self.side *= factor
        return self

class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def scale(self, factor: float) -> 'Rectangle':
        self.width *= factor
        self.height *= factor
        return self

def calculate_area(shape: Shape) -> float:
    return shape.area()

def scale_shape(shape: Shape, factor: float) -> Shape:
    return shape.scale(factor)

if __name__ == '__main__':
    circle = Circle(5.0)
    square = Square(4.0)
    rectangle = Rectangle(2.0, 6.0)

    print(calculate_area(circle))
    print(calculate_area(square))
    print(calculate_area(rectangle))

    scale_shape(circle, 2.0)
    scale_shape(square, 0.5)
    scale_shape(rectangle, 3.0)

    print(circle.area())
    print(square.area())
    print(rectangle.area())