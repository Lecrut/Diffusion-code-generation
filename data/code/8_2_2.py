class Shape:
    def calculate_area(self):
        raise NotImplementedError("Subclasses must implement calculate_area method")
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def calculate_area(self):
        return self.length * self.width
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        import math
        return math.pi * self.radius**2
if __name__ == '__main__':
    rectangle = Rectangle(10, 5)
    circle = Circle(7)
    print("Rectangle Area:", rectangle.calculate_area())
    print("Circle Area:", circle.calculate_area())