import math

class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

    def get_radius(self):
        return self.radius

if __name__ == '__main__':
    sample_radii = [4, 9, 16]
    for radius in sample_radii:
        circle = Circle(radius)
        area = circle.calculate_area()
        print(f"The area of a circle with radius {circle.get_radius()} is: {area:.2f}")