import math

class Circle:
    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = diameter / 2

    def area(self):
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    sample_diameters = [10, 20, 30]
    for diameter in sample_diameters:
        circle = Circle(diameter)
        print(f"Area of circle with diameter {diameter}: {circle.area()}")