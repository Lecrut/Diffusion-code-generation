import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def validate_radius(self):
        if self.radius < 0:
            raise ValueError("Radius cannot be negative")

    def area(self):
        self.validate_radius()
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    sample_radius = 10.0
    circle_instance = Circle(sample_radius)
    try:
        print(circle_instance.area())
    except ValueError as e:
        print(e)