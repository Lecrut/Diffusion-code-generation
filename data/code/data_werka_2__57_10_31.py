import math

class CircleGeometry:
    def __init__(self, radius):
        self.radius = radius
        if radius < 0:
            raise ValueError("Radius cannot be negative")

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    sample_radius = 5
    circle_geometry = CircleGeometry(sample_radius)
    print(circle_geometry.calculate_area())