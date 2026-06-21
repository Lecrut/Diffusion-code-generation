import math

class Shape:
    def calculate_area(self):
        raise ValueError("This method should be overridden by subclasses")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def validate_radius(self):
        if self.radius < 0:
            raise ValueError("Radius cannot be negative")

    def calculate_area(self):
        self.validate_radius()
        return math.pi * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def validate_dimensions(self):
        if self.width < 0 or self.height < 0:
            raise ValueError("Width and height cannot be negative")

    def calculate_area(self):
        self.validate_dimensions()
        return self.width * self.height

if __name__ == '__main__':
    circle = Circle(radius=5.0)
    rectangle = Rectangle(width=4.0, height=6.0)

    print("Circle Area:", circle.calculate_area())
    print("Rectangle Area:", rectangle.calculate_area())