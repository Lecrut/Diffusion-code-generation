import math

class GeometricShape:
    def __init__(self, name: str, area: float) -> None:
        self.name = name
        self.area = area

    def calculate_area(self) -> float:
        return self.area

    def scale_area(self, factor: float) -> float:
        self.area = self.area * factor
        return self.area

class Circle(GeometricShape):
    def __init__(self, radius: float) -> None:
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius
        super().__init__("Circle", math.pi * (radius ** 2))

class Rectangle(GeometricShape):
    def __init__(self, width: float, height: float) -> None:
        if width < 0 or height < 0:
            raise ValueError("Dimensions cannot be negative")
        self.width = width
        self.height = height
        super().__init__("Rectangle", width * height)

if __name__ == '__main__':
    circle = Circle(5.0)
    scaled_circle_area = circle.scale_area(2.0)
    print(scaled_circle_area)

    rectangle = Rectangle(4.0, 6.0)
    scaled_rectangle_area = rectangle.scale_area(3.0)
    print(scaled_rectangle_area)