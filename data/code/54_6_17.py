import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @staticmethod
    def area(radius):
        return math.pi * (radius ** 2)

if __name__ == '__main__':
    sample_radius = 10
    circle = Circle(sample_radius)
    print(Circle.area(sample_radius))