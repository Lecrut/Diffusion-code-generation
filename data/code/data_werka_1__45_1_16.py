import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        if self.radius < 0:
            raise ValueError("Radius cannot be negative")
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    sample_radius = 3.5
    circle = Circle(sample_radius)
    print(circle.area())