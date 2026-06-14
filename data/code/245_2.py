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
    area1_circle = circle1.calculate_area()
    area1_rectangle = rectangle1.calculate_area()
    area2_circle = circle2.calculate_area()
    area2_rectangle = rectangle2.calculate_area()
    print(f"Area of Circle 1: {area1_circle}")
    print(f"Area of Rectangle 1: {area1_rectangle}")
    print(f"Area of Circle 2: {area2_circle}")
    print(f"Area of Rectangle 2: {area2_rectangle}")
    print(f"Are the areas of the two circles equal? {area1_circle == area2_circle}")
    print(f"Are the areas of the two rectangles equal? {area1_rectangle == area2_rectangle}")