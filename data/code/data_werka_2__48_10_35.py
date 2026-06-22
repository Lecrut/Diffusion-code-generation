import math

class Rectangle:
    def __init__(self, width, height):
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
    rect = Rectangle(5.0, 3.0)
    print(f"Perimeter: {rect.perimeter()}")
    print(f"Area: {rect.area()}")