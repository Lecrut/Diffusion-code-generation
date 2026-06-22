import math

PI = math.pi

class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def area(self):
        return PI * self.radius ** 2

if __name__ == '__main__':
    try:
        sample_radius = -3.0
        circle = Circle(sample_radius)
        print(circle.area())
    except ValueError as e:
        print(e)