import math

class Rectangle:
    WIDTH = 5.0
    HEIGHT = 3.0
    
    @staticmethod
    def calculate_perimeter(width, height):
        return 2 * (width + height)
    
    @staticmethod
    def calculate_area(width, height):
        return width * height
    
    def __init__(self, width=WIDTH, height=HEIGHT):
        self.width = width
        self.height = height
    
    def perimeter(self):
        return Rectangle.calculate_perimeter(self.width, self.height)
    
    def area(self):
        return Rectangle.calculate_area(self.width, self.height)

if __name__ == '__main__':
    rect = Rectangle()
    print(f"Perimeter: {rect.perimeter()}")
    print(f"Area: {rect.area()}")