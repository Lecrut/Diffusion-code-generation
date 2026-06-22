import math

class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

    def describe(self):
        return f"Circle with radius {self.radius}"

if __name__ == '__main__':
    sample_radii = [4, 9, 12]
    for radius in sample_radii:
        circle = Circle(radius)
        area = circle.calculate_area()
        description = circle.describe()
        print(f"{description} has an area of: {area:.2f}")