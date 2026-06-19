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

class Square(GeometricShape):
    def __init__(self, side_length: float):
        super().__init__(side_length ** 2)

if __name__ == '__main__':
    circle = Circle(radius=5.0)
    square = Square(side_length=4.0)

    print("Original Circle Area:", circle.calculate_area())
    print("Original Square Area:", square.calculate_area())

    circle.scale_area(2.0)
    square.scale_area(1.5)

    print("Scaled Circle Area:", circle.calculate_area())
    print("Scaled Square Area:", square.calculate_area())