import math

class Circle:
    PI = math.pi

    @staticmethod
    def validate_radius(radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")

    def __init__(self, radius):
        self.validate_radius(radius)
        self.radius = radius

    def calculate_area(self):
        return self.PI * (self.radius ** 2)

if __name__ == '__main__':
    sample_radii = [4, 9, 16]
    for index, radius in enumerate(sample_radii, start=1):
        try:
            circle = Circle(radius)
            area = circle.calculate_area()
            print(f"Sample {index}: The area of a circle with radius {radius} is {area:.2f}")
        except ValueError as e:
            print(e)