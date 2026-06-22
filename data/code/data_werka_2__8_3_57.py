import math

class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    sample_radius_1 = 4.0
    circle_1 = Circle(sample_radius_1)
    print(circle_1.area())

    sample_radius_2 = 6.5
    circle_2 = Circle(sample_radius_2)
    print(circle_2.area())