import math

class AreaCalculator:
    def __init__(self, figure):
        self.figure = figure

    def compute(self):
        return self.figure.get_area()

class Shape:
    def get_area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, dim_a, dim_b):
        self.dim_a = dim_a
        self.dim_b = dim_b

    def get_area(self):
        return self.dim_a * self.dim_b

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    rect = Rectangle(5, 8)
    circ = Circle(3)
    rect_calc = AreaCalculator(rect)
    circ_calc = AreaCalculator(circ)
    print(rect_calc.compute())
    print(circ_calc.compute())