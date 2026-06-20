import math
from typing import List

PI = math.pi

class Shape:
    def __init__(self, name: str) -> None:
        self.name = name

    def area(self) -> float:
        return 0.0

    def scale_dimensions(self, factor: float) -> None:
        if factor <= 0:
            raise ValueError("Scale factor must be positive")

    def get_scaled_area(self, factor: float) -> float:
        self.scale_dimensions(factor)
        return self.area()

class Circle(Shape):
    def __init__(self, radius: float) -> None:
        super().__init__("Circle")
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def area(self) -> float:
        return PI * self.radius * self.radius

    def scale_dimensions(self, factor: float) -> None:
        super().scale_dimensions(factor)
        self.radius *= factor

class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        super().__init__("Rectangle")
        if width < 0 or height < 0:
            raise ValueError("Dimensions cannot be negative")
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def scale_dimensions(self, factor: float) -> None:
        super().scale_dimensions(factor)
        self.width *= factor
        self.height *= factor

class Triangle(Shape):
    def __init__(self, base: float, height: float) -> None:
        super().__init__("Triangle")
        if base < 0 or height < 0:
            raise ValueError("Base and height cannot be negative")
        self.base = base
        self.height = height

    def area(self) -> float:
        return 0.5 * self.base * self.height

    def scale_dimensions(self, factor: float) -> None:
        super().scale_dimensions(factor)
        self.base *= factor
        self.height *= factor

if __name__ == '__main__':
    shapes: List[Shape] = []
    shapes.append(Circle(5.0))
    shapes.append(Rectangle(10.0, 4.0))
    shapes.append(Triangle(6.0, 8.0))

    scale_factor = 1.5

    for shape in shapes:
        original_area = shape.area()
        new_area = shape.get_scaled_area(scale_factor)
        print(f"Shape: {shape.name}, Original Area: {original_area:.2f}, Scaled Area: {new_area:.2f}")