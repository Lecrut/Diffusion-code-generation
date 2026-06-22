import math

CIRCLE_AREA_COEFF = 3.14
RECTANGLE_AREA_COEFF = 2.0

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return CIRCLE_AREA_COEFF * self.radius ** 2

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return RECTANGLE_AREA_COEFF * self.width * self.height

def compare_areas(circle, rectangle):
    circle_area = circle.area()
    rectangle_area = rectangle.area()
    if circle_area > rectangle_area:
        return "Circle is larger"
    elif circle_area < rectangle_area:
        return "Rectangle is larger"

if __name__ == '__main__':
    circle = Circle(5)
    rectangle = Rectangle(4, 3)
    
    print("Circle area:", circle.area())
    print("Rectangle area:", rectangle.area())
    print(compare_areas(circle, rectangle))