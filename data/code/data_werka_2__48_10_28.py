import math

class Rectangle:
    WIDTH = 5.0
    HEIGHT = 3.0
    
    def __init__(self, width=WIDTH, height=HEIGHT):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive numbers.")
        self.width = width
        self.height = height
    
    @staticmethod
    def calculate_perimeter(width, height):
        return 2 * (width + height)
    
    @staticmethod
    def calculate_area(width, height):
        return width * height
    
    def perimeter(self):
        return Rectangle.calculate_perimeter(self.width, self.height)
    
    def area(self):
        return Rectangle.calculate_area(self.width, self.height)

if __name__ == '__main__':
    rect = Rectangle()
    print(f"Perimeter: {rect.perimeter()}")
    print(f"Area: {rect.area()}")