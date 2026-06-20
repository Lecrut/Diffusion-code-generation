import math
from typing import List

class Shape:
    def area(self) -> float:
        raise RuntimeError("Subclass must implement area")

    def scale(self, factor: float) -> None:
        if factor <= 0:
            raise ValueError("Factor must be positive")

    def scaled_area(self, factor: float) -> float:
        original_area = self.area()
        return original_area * (factor ** 2)

class Triangle(Shape):
    def __init__(self, base: float, height: float) -> None:
        if base <= 0 or height <= 0:
            raise ValueError("Dimensions must be positive")
        self.base = base
        self.height = height

    def area(self) -> float:
        return 0.5 * self.base * self.height

    def scale(self, factor: float) -> None:
        super().scale(factor)
        self.base *= factor
        self.height *= factor

class Square(Shape):
    def __init__(self, side: float) -> None:
        if side <= 0:
            raise ValueError("Side must be positive")
        self.side = side

    def area(self) -> float:
        return self.side ** 2

    def scale(self, factor: float) -> None:
        super().scale(factor)
        self.side *= factor

def process_shapes(shapes: List[Shape], factor: float) -> List[float]:
    results = []
    for shape in shapes:
        results.append(shape.scaled_area(factor))
    return results

if __name__ == '__main__':
    triangle = Triangle(10.0, 5.0)
    square = Square(4.0)
    shapes = [triangle, square]
    factor = 2.5
    areas = process_shapes(shapes, factor)
    print(areas[0])
    print(areas[1])
    triangle.scale(3.0)
    print(triangle.area())