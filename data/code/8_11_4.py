import math

class Circle:
    def __init__(self, radius: float) -> None:
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius: float = radius

    def area(self) -> float:
        return math.pi * (self.radius ** 2)

    def scale(self, factor: float) -> None:
        if factor <= 0:
            raise ValueError("Scale factor must be positive")
        self.radius *= factor

    def scaled_area(self, factor: float) -> float:
        if factor <= 0:
            raise ValueError("Scale factor must be positive")
        return self.area() * (factor ** 2)

class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        if width <= 0 or height <= 0:
            raise ValueError("Dimensions must be positive")
        self.width: float = width
        self.height: float = height

    def area(self) -> float:
        return self.width * self.height

    def scale(self, factor: float) -> None:
        if factor <= 0:
            raise ValueError("Scale factor must be positive")
        self.width *= factor
        self.height *= factor

    def scaled_area(self, factor: float) -> float:
        if factor <= 0:
            raise ValueError("Scale factor must be positive")
        return self.area() * (factor ** 2)

if __name__ == '__main__':
    circle = Circle(radius=5.0)
    circle_area = circle.area()
    print(f"Circle Area: {circle_area}")

    circle.scale(factor=2.0)
    scaled_circle_area = circle.scaled_area(factor=1.0)
    print(f"Scaled Circle Area: {scaled_circle_area}")

    rectangle = Rectangle(width=4.0, height=6.0)
    rect_area = rectangle.area()
    print(f"Rectangle Area: {rect_area}")

    rectangle.scale(factor=3.0)
    scaled_rect_area = rectangle.scaled_area(factor=1.0)
    print(f"Scaled Rectangle Area: {scaled_rect_area}")