import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @staticmethod
    def calculate_area(radius):
        return math.pi * radius * radius

if __name__ == '__main__':
    sample_radius = 7.0
    circle = Circle(sample_radius)
    area = Circle.calculate_area(circle.radius)
    print(area)