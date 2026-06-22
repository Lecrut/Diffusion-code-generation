import math

class GeometricShape:
    def __init__(self, name: str) -> None:
        self.name = name

    def get_area(self) -> float:
        raise ValueError("Method must be implemented in subclass")

    def scale(self, factor: float) -> None:
        if factor <= 0:
            raise ValueError("Scale factor must be positive")

class Circle(GeometricShape):
    def __init__(self, radius: float, name: str = "Circle") -> None:
        super().__init__(name)
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius

    def get_area(self) -> float:
        return math.pi * (self.radius ** 2)

    def scale(self, factor: float) -> None:
        super().scale(factor)
        self.radius *= factor

class Rectangle(GeometricShape):
    def __init__(self, width: float, height: float, name: str = "Rectangle") -> None:
        super().__init__(name)
        if width <= 0 or height <= 0:
            raise ValueError("Dimensions must be positive")
        self.width = width
        self.height = height

    def get_area(self) -> float:
        return self.width * self.height

    def scale(self, factor: float) -> None:
        super().scale(factor)
        self.width *= factor
        self.height *= factor

class Triangle(GeometricShape):
    def __init__(self, base: float, height: float, name: str = "Triangle") -> None:
        super().__init__(name)
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive")
        self.base = base
        self.height = height

    def get_area(self) -> float:
        return 0.5 * self.base * self.height

    def scale(self, factor: float) -> None:
        super().scale(factor)
        self.base *= factor
        self.height *= factor

def calculate_scaled_area(shape: GeometricShape, factor: float) -> float:
    original_area = shape.get_area()
    shape.scale(factor)
    return shape.get_area()

if __name__ == '__main__':
    circle = Circle(radius=5.0)
    circle_area = circle.get_area()
    scaled_circle_area = calculate_scaled_area(circle, 2.0)

    rectangle = Rectangle(width=4.0, height=6.0)
    rectangle_area = rectangle.get_area()
    scaled_rectangle_area = calculate_scaled_area(rectangle, 3.0)

    triangle = Triangle(base=10.0, height=5.0)
    triangle_area = triangle.get_area()
    scaled_triangle_area = calculate_scaled_area(triangle, 0.5)

    print(f"Original Circle Area: {circle_area}")
    print(f"Scaled Circle Area: {scaled_circle_area}")
    print(f"Original Rectangle Area: {rectangle_area}")
    print(f"Scaled Rectangle Area: {scaled_rectangle_area}")
    print(f"Original Triangle Area: {triangle_area}")
    print(f"Scaled Triangle Area: {scaled_triangle_area}")