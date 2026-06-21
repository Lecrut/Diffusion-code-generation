import math

class Shape:
    def calculate_area(self):
        raise ValueError("This method should be overridden by subclasses")

class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius
    
    def calculate_area(self):
        return math.pi * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive")
        self.width = width
        self.height = height
    
    def calculate_area(self):
        return self.width * self.height

if __name__ == '__main__':
    try:
        circle = Circle(radius=5.0)
        print(f"Circle area: {circle.calculate_area()}")
        
        rectangle = Rectangle(width=4.0, height=6.0)
        print(f"Rectangle area: {rectangle.calculate_area()}")
        
    except ValueError as e:
        print(e)