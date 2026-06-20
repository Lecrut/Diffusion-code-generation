import math

class Shape:
    def __init__(self, base_dimension, height=None):
        self.base_dimension = base_dimension
        self.height = height

    def get_base_area(self):
        return 0.0

    def calculate_scaled_area(self, scale_factor):
        base_area = self.get_base_area()
        return base_area * (scale_factor ** 2)

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__(width, height)

    def get_base_area(self):
        return self.base_dimension * self.height

class Circle(Shape):
    def __init__(self, radius):
        super().__init__(radius)

    def get_base_area(self):
        return math.pi * (self.base_dimension ** 2)

if __name__ == '__main__':
    rect = Rectangle(10, 5)
    circle = Circle(3)
    scale_factor = 2.5

    rect_scaled = rect.calculate_scaled_area(scale_factor)
    circle_scaled = circle.calculate_scaled_area(scale_factor)

    print(rect_scaled)
    print(circle_scaled)