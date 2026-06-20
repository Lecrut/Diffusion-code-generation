import math
from typing import List, Union

class Shape:
    def __init__(self, name: str) -> None:
        self.name = name

    def area(self) -> float:
        return 0.0

    def scale(self, factor: float) -> None:
        if factor <= 0:
            raise ValueError("Scale factor must be positive")
        self._scale_internal(factor)

    def _scale_internal(self, factor: float) -> None:
        raise ValueError("Subclasses must implement _scale_internal")

class Circle(Shape):
    def __init__(self, radius: float) -> None:
        super().__init__("Circle")
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def _scale_internal(self, factor: float) -> None:
        self.radius *= factor

class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def _scale_internal(self, factor: float) -> None:
        self.width *= factor
        self.height *= factor

def calculate_scaled_area(shape: Shape, factor: float) -> float:
    original_area = shape.area()
    shape.scale(factor)
    new_area = shape.area()
    shape.scale(1.0 / factor)
    return new_area

if __name__ == '__main__':
    circle = Circle(5.0)
    rectangle = Rectangle(4.0, 6.0)
    
    scale_factor = 2.0
    
    scaled_circle_area = calculate_scaled_area(circle, scale_factor)
    scaled_rectangle_area = calculate_scaled_area(rectangle, scale_factor)
    
    print(scaled_circle_area)
    print(scaled_rectangle_area)