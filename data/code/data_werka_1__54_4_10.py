import math

class Circle:
    def __init__(self, diameter):
        self.diameter = diameter

    def calculate_radius(self):
        return self.diameter / 2

    def calculate_area(self):
        radius = self.calculate_radius()
        return math.pi * (radius ** 2)

if __name__ == '__main__':
    sample_diameters = [10, 25, 50]
    for diameter in sample_diameters:
        circle = Circle(diameter)
        print(f"Area of a circle with diameter {diameter}: {circle.calculate_area()}")