import math

class Circle:
    def __init__(self, radius: float) -> None:
        if radius < 0:
            raise ValueError("Radius must be non-negative")
        self.radius = radius

    def area(self) -> float:
        return math.pi * (self.radius ** 2)

    def scale(self, factor: float) -> None:
        if factor < 0:
            raise ValueError("Scale factor must be non-negative")
        self.radius *= factor

    def scaled_area(self, factor: float) -> float:
        if factor < 0:
            raise ValueError("Scale factor must be non-negative")
        return self.area() * (factor ** 2)

class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        if width < 0 or height < 0:
            raise ValueError("Dimensions must be non-negative")
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def scale(self, factor: float) -> None:
        if factor < 0:
            raise ValueError("Scale factor must be non-negative")
        self.width *= factor
        self.height *= factor

    def scaled_area(self, factor: float) -> float:
        if factor < 0:
            raise ValueError("Scale factor must be non-negative")
        return self.area() * (factor ** 2)

if __name__ == '__main__':
    circle = Circle(5.0)
    print(circle.area())
    circle.scale(2.0)
    print(circle.area())
    print(circle.scaled_area(3.0))

    rectangle = Rectangle(4.0, 6.0)
    print(rectangle.area())
    rectangle.scale(0.5)
    print(rectangle.area())
    print(rectangle.scaled_area(2.0))