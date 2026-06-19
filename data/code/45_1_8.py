import math

class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    try:
        sample_radius = 10.0
        circle_instance = Circle(sample_radius)
        print(circle_instance.area())
    except ValueError as e:
        print(e)