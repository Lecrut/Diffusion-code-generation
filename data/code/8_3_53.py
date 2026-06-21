import math

class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    sample_radius = 10
    circle = Circle(sample_radius)
    area = circle.calculate_area()
    print(area)