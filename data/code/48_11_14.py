import math

def calculate_perimeter(width, height):
    return 2 * (width + height)

def calculate_area(width, height):
    return width * height

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def get_perimeter(self):
        return calculate_perimeter(self.width, self.height)
    
    def get_area(self):
        return calculate_area(self.width, self.height)

if __name__ == '__main__':
    sample_width = 7.5
    sample_height = 2.0
    rect = Rectangle(sample_width, sample_height)
    perimeter_result = rect.get_perimeter()
    area_result = rect.get_area()
    print(f"Perimeter: {perimeter_result}")
    print(f"Area: {area_result}")