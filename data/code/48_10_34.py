import math

def calculate_perimeter(width, height):
    return 2 * (width + height)

def calculate_area(width, height):
    return width * height

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def perimeter(self):
        return calculate_perimeter(self.width, self.height)
    
    def area(self):
        return calculate_area(self.width, self.height)

if __name__ == '__main__':
    rect = Rectangle(5.0, 3.0)
    print(f"Perimeter: {rect.perimeter()}")
    print(f"Area: {rect.area()}")