import math
WIDTH = 5.0
HEIGHT = 3.0

class Rectangle:

    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError('Width and height must be positive numbers.')
        self.width = width
        self.height = height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

    def calculate_area(self):
        return self.width * self.height
if __name__ == '__main__':
    try:
        rect = Rectangle(WIDTH, HEIGHT)
        print(f'Perimeter: {rect.calculate_perimeter()}')
        print(f'Area: {rect.calculate_area()}')
    except ValueError as e:
        print(e)