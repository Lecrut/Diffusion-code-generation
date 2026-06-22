import math

class Shape:
    def calculate_area(self):
        raise ValueError("Subclasses should implement this method")

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
    circle1 = Circle(radius=5)
    rectangle1 = Rectangle(width=7, height=3)
    
    print(f"Circle Area: {circle1.calculate_area()}")
    print(f"Rectangle Area: {rectangle1.calculate_area()}")