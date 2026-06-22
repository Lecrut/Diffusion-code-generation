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

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        super().__init__(width * height)

class Circle(Shape):
    def __init__(self, radius: float):
        super().__init__(3.14159 * radius ** 2)

if __name__ == '__main__':
    rectangle = Rectangle(width=5.0, height=3.0)
    circle = Circle(radius=4.0)

    print("Original Rectangle Area:", rectangle.get_area())
    rectangle.scale_area(2.0)
    print("Scaled Rectangle Area:", rectangle.get_area())

    print("Original Circle Area:", circle.get_area())
    circle.scale_area(1.5)
    print("Scaled Circle Area:", circle.get_area())