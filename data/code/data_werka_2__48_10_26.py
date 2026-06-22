import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def area(self):
        return self.width * self.height

def calculate_rectangle_properties(width, height):
    rect = Rectangle(width, height)
    return rect.perimeter(), rect.area()

if __name__ == '__main__':
    rectangle_dimensions = {
        'width': 5.0,
        'height': 3.0
    }
    
    perimeter, area = calculate_rectangle_properties(rectangle_dimensions['width'], rectangle_dimensions['height'])
    print(f"Perimeter: {perimeter}")
    print(f"Area: {area}")