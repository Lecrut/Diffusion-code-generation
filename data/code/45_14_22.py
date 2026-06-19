import math

class Circle:
    PI = math.pi

    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative.")
        self.radius = radius

    @staticmethod
    def calculate_area(radius):
        return Circle.PI * (radius ** 2)

if __name__ == '__main__':
    sample_radius = 3.5
    circle = Circle(sample_radius)
    print(circle.calculate_area(sample_radius))