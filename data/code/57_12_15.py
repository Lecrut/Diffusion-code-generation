import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

if __name__ == '__main__':
    circle = Circle(5)
    area = circle.calculate_area()
    print(area)