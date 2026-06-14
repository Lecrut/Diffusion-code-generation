import math
class Shape:
    def calculate_area(self):
        raise NotImplementedError("Subclasses must implement this method")
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        return math.pi * self.radius**2
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def calculate_area(self):
        return self.length * self.width
if __name__ == '__main__':
    circle1 = Circle(5)
    rectangle1 = Rectangle(4, 6)
    circle2 = Circle(5)
    rectangle2 = Rectangle(4, 6)
    area1 = circle1.calculate_area()
    area2 = rectangle2.calculate_area()
    print(f"Area of Circle 1: {area1}")
    print(f"Area of Rectangle 2: {area2}")
    if area1 == area2:
        print("The areas are equal.")
    else:
        print("The areas are not equal.")