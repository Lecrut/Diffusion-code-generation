import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @staticmethod
    def calculate_circumference(radius):
        return 2 * math.pi * radius

if __name__ == '__main__':
    sample_radius = 3.14
    circle = Circle(sample_radius)
    circumference = circle.calculate_circumference(circle.radius)
    print(circumference)