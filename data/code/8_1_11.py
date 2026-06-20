import math

PI = 3.141592653589793

class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return PI * self.radius * self.radius

def print_area(shape, name):
    result = shape.area()
    print(f"{name}: {result}")
    return result

if __name__ == '__main__':
    rect_instance = Rectangle(4, 7)
    circle_instance = Circle(3)
    print_area(rect_instance, "RectangleArea")
    print_area(circle_instance, "CircleArea")