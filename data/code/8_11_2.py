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

    def scaled_area(self, factor: float) -> float:
        self.scale(factor)
        return self.area()

class Circle(Shape):
    def __init__(self, radius: float) -> None:
        super().__init__("Circle")
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius * self.radius

    def scale(self, factor: float) -> None:
        super().scale(factor)
        self.radius *= factor

class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def scale(self, factor: float) -> None:
        super().scale(factor)
        self.width *= factor
        self.height *= factor

class Triangle(Shape):
    def __init__(self, base: float, height: float) -> None:
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def area(self) -> float:
        return 0.5 * self.base * self.height

    def scale(self, factor: float) -> None:
        super().scale(factor)
        self.base *= factor
        self.height *= factor

def calculate_and_scale_all(shapes: List[Shape], factor: float) -> List[float]:
    results: List[float] = []
    for shape in shapes:
        area = shape.scaled_area(factor)
        results.append(area)
    return results

if __name__ == '__main__':
    circle = Circle(5.0)
    rectangle = Rectangle(10.0, 4.0)
    triangle = Triangle(6.0, 8.0)

    shapes: List[Shape] = [circle, rectangle, triangle]
    scale_factor: float = 2.0

    areas = calculate_and_scale_all(shapes, scale_factor)

    print(f"Circle scaled area: {areas[0]:.2f}")
    print(f"Rectangle scaled area: {areas[1]:.2f}")
    print(f"Triangle scaled area: {areas[2]:.2f}")