from typing import Union

class Shape:
    def __init__(self, area: float):
        self.area = area

    def scale_area(self, factor: float) -> None:
        if factor <= 0:
            raise ValueError("Scale factor must be positive")
        self.area *= factor

    def get_area(self) -> float:
        return self.area

class Circle(Shape):
    def __init__(self, radius: float):
        super().__init__(3.14159 * radius ** 2)

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        super().__init__(width * height)

if __name__ == '__main__':
    circle = Circle(radius=5)
    rectangle = Rectangle(width=4, height=6)

    print("Original Circle Area:", circle.get_area())
    circle.scale_area(2)
    print("Scaled Circle Area:", circle.get_area())

    print("Original Rectangle Area:", rectangle.get_area())
    rectangle.scale_area(0.5)
    print("Scaled Rectangle Area:", rectangle.get_area())