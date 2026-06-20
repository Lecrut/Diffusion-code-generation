import math
from typing import List

class GeometricShape:
    def __init__(self, area: float) -> None:
        self.area = area

    def get_area(self) -> float:
        return self.area

    def scale_area(self, factor: float) -> float:
        self.area = self.area * factor
        return self.area

class Circle(GeometricShape):
    def __init__(self, radius: float) -> None:
        if radius <= 0:
            raise ValueError("Radius must be positive")
        area = math.pi * (radius ** 2)
        super().__init__(area)
        self.radius = radius

    def __repr__(self) -> str:
        return f"Circle(radius={self.radius}, area={self.get_area()})"

class Rectangle(GeometricShape):
    def __init__(self, width: float, height: float) -> None:
        if width <= 0 or height <= 0:
            raise ValueError("Dimensions must be positive")
        area = width * height
        super().__init__(area)
        self.width = width
        self.height = height

    def __repr__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height}, area={self.get_area()})"

def calculate_total_area(shapes: List[GeometricShape]) -> float:
    total = 0.0
    for shape in shapes:
        total += shape.get_area()
    return total

if __name__ == '__main__':
    circle = Circle(5.0)
    rectangle = Rectangle(4.0, 6.0)
    
    initial_area = circle.get_area()
    print(initial_area)
    
    scaled_area = circle.scale_area(2.0)
    print(scaled_area)
    
    total_area = calculate_total_area([circle, rectangle])
    print(total_area)