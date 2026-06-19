import math
PI = math.pi

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return PI * self.radius ** 2

    def perimeter(self):
        return 2 * PI * self.radius

class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)
if __name__ == '__main__':
    circle_radius = 7
    rectangle_length = 8
    rectangle_width = 3
    circle = Circle(circle_radius)
    rectangle = Rectangle(rectangle_length, rectangle_width)
    print(f'Circle Dimensions: Radius = {circle_radius}')
    print(f'Calculated Circle Area: {circle.area()}')
    print(f'Calculated Circle Perimeter: {circle.perimeter()}')
    print('-' * 30)
    print(f'Rectangle Dimensions: Length = {rectangle_length}, Width = {rectangle_width}')
    print(f'Calculated Rectangle Area: {rectangle.area()}')
    print(f'Calculated Rectangle Perimeter: {rectangle.perimeter()}')