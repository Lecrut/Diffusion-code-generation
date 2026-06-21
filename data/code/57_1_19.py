import math

class Shape:
    def calculate_area(self):
        raise ValueError("This method should be overridden by subclasses")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return math.pi * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculate_area(self):
        return self.width * self.height

if __name__ == '__main__':
    circle_radius = 7.0
    rectangle_width = 3.0
    rectangle_height = 8.0

    circle = Circle(circle_radius)
    rectangle = Rectangle(rectangle_width, rectangle_height)

    print(f"Circle area with radius {circle_radius}: {circle.calculate_area()}")
    print(f"Rectangle area with width {rectangle_width} and height {rectangle_height}: {rectangle.calculate_area()}")