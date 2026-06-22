import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

if __name__ == '__main__':
    sample_circle = Circle(5.0)
    print(sample_circle.area())
    another_circle = Circle(10.0)
    print(another_circle.area())