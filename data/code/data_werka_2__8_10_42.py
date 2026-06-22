from typing import Union

class Shape:
    def __init__(self, area: float):
        self.area = area

    def calculate_area(self) -> float:
        return self.area

    def scale_area(self, factor: float) -> None:
        if factor <= 0:
            raise ValueError("Scale factor must be positive")
        self.area *= factor

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        super().__init__(width * height)

class Circle(Shape):
    def __init__(self, radius: float):
        super().__init__(3.14159 * radius ** 2)

if __name__ == '__main__':
    rectangle = Rectangle(width=5.0, height=3.0)
    print("Original Rectangle Area:", rectangle.calculate_area())

    circle = Circle(radius=4.0)
    print("Original Circle Area:", circle.calculate_area())

    scale_factor = 2.0
    rectangle.scale_area(scale_factor)
    print(f"Scaled Rectangle Area by {scale_factor}:", rectangle.calculate_area())

    circle.scale_area(scale_factor)
    print(f"Scaled Circle Area by {scale_factor}:", circle.calculate_area())