import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculate_perimeter(self):
        return 2 * (self.width + self.height)
    
    def calculate_area(self):
        return self.width * self.height

if __name__ == '__main__':
    rect = Rectangle(5.0, 3.0)
    print("Perimeter:", rect.calculate_perimeter())
    print("Area:", rect.calculate_area())