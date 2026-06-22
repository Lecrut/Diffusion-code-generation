import math

class Circle:
    PI = 3.14
    
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius
    
    @staticmethod
    def area(radius):
        return Circle.PI * radius ** 2

class Rectangle:
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive")
        self.width = width
        self.height = height
    
    @staticmethod
    def area(width, height):
        return width * height

def compare_areas(circle_radius, rectangle_width, rectangle_height):
    circle_area = Circle.area(circle_radius)
    rectangle_area = Rectangle.area(rectangle_width, rectangle_height)
    
    if circle_area > rectangle_area:
        return "Circle is larger"
    elif circle_area < rectangle_area:
        return "Rectangle is larger"

if __name__ == '__main__':
    print(compare_areas(5, 10, 2))