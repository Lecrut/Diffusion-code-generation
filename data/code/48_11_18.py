import math

def calculate_perimeter(width, height):
    return 2 * (width + height)

def calculate_area(width, height):
    return width * height

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def get_properties(self):
        perimeter = calculate_perimeter(self.width, self.height)
        area = calculate_area(self.width, self.height)
        return perimeter, area

if __name__ == '__main__':
    rect = Rectangle(5.0, 3.0)
    perimeter, area = rect.get_properties()
    print(f"Perimeter: {perimeter}")
    print(f"Area: {area}")