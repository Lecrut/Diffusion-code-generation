from typing import Union

class GeometricShape:
    def __init__(self, area: float):
        self.area = area

    def calculate_area(self) -> float:
        return self.area

    def scale_area(self, factor: float) -> None:
        self.area *= factor

class Circle(GeometricShape):
    def __init__(self, radius: float):
        super().__init__(3.14159 * radius ** 2)

class Rectangle(GeometricShape):
    def __init__(self, width: float, height: float):
        super().__init__(width * height)

if __name__ == '__main__':
    circle = Circle(radius=5)
    rectangle = Rectangle(width=4, height=6)

    print("Original Circle Area:", circle.calculate_area())
    print("Original Rectangle Area:", rectangle.calculate_area())

    circle.scale_area(2)
    rectangle.scale_area(1.5)

    print("Scaled Circle Area:", circle.calculate_area())
    print("Scaled Rectangle Area:", rectangle.calculate_area())