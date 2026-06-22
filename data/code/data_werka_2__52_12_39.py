import math

class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    sample_radius1 = 3.0
    sample_radius2 = 8.5
    circle1 = Circle(sample_radius1)
    circle2 = Circle(sample_radius2)
    print(circle1.area())
    print(circle2.area())