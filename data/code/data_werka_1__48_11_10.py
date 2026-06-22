import math

def validate_dimensions(width, height):
    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be positive numbers.")

def calculate_perimeter(width, height):
    return 2 * (width + height)

def calculate_area(width, height):
    return width * height

class Rectangle:
    def __init__(self, width, height):
        validate_dimensions(width, height)
        self.width = width
        self.height = height
    
    def perimeter(self):
        return calculate_perimeter(self.width, self.height)
    
    def area(self):
        return calculate_area(self.width, self.height)

if __name__ == '__main__':
    width_val = 5.0
    height_val = 3.0
    rect = Rectangle(width_val, height_val)
    print(f"Perimeter: {rect.perimeter()}")
    print(f"Area: {rect.area()}")