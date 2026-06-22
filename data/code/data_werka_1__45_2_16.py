import math

class Circle:
    def __init__(self, diameter):
        if diameter <= 0:
            raise ValueError("Diameter must be positive")
        self.diameter = diameter
        self.radius = diameter / 2

    def area(self):
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    sample_diameters = [7, 15, -2, 0]
    for diameter in sample_diameters:
        try:
            circle = Circle(diameter)
            print(f"Area of circle with diameter {diameter}: {circle.area()}")
        except ValueError as e:
            print(f"Error for diameter {diameter}: {e}")