import math

def calculate_perimeter(width, height):
    return 2 * (width + height)

def calculate_area(width, height):
    return width * height

class Rectangle:
    def __init__(self, dimensions):
        if dimensions['width'] <= 0 or dimensions['height'] <= 0:
            raise ValueError("Width and height must be positive numbers.")
        self.width = dimensions['width']
        self.height = dimensions['height']

    def perimeter(self):
        return calculate_perimeter(self.width, self.height)

    def area(self):
        return calculate_area(self.width, self.height)

if __name__ == '__main__':
    rectangle_dimensions = {
        'width': 5.0,
        'height': 3.0
    }
    rect = Rectangle(rectangle_dimensions)
    print(f"Perimeter: {rect.perimeter()}")
    print(f"Area: {rect.area()}")