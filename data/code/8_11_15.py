import math

class Triangle:
    def __init__(self, base: float, height: float) -> None:
        if base <= 0 or height <= 0:
            raise ValueError("Dimensions must be positive")
        self.base = base
        self.height = height

    def calculate_area(self) -> float:
        return 0.5 * self.base * self.height

    def scale_area(self, factor: float) -> float:
        if factor <= 0:
            raise ValueError("Scale factor must be positive")
        return self.calculate_area() * (factor ** 2)

class Circle:
    def __init__(self, radius: float) -> None:
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius

    def calculate_area(self) -> float:
        return math.pi * self.radius ** 2

    def scale_area(self, factor: float) -> float:
        if factor <= 0:
            raise ValueError("Scale factor must be positive")
        return self.calculate_area() * (factor ** 2)

class Square:
    def __init__(self, side: float) -> None:
        if side <= 0:
            raise ValueError("Side length must be positive")
        self.side = side

    def calculate_area(self) -> float:
        return self.side ** 2

    def scale_area(self, factor: float) -> float:
        if factor <= 0:
            raise ValueError("Scale factor must be positive")
        return self.calculate_area() * (factor ** 2)

if __name__ == '__main__':
    triangle = Triangle(10.0, 5.0)
    print(triangle.calculate_area())
    print(triangle.scale_area(2.0))

    circle = Circle(4.0)
    print(circle.calculate_area())
    print(circle.scale_area(1.5))

    square = Square(6.0)
    print(square.calculate_area())
    print(square.scale_area(3.0))