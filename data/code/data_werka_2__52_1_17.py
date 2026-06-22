import math

class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

if __name__ == '__main__':
    sample_radius1 = 4.0
    sample_radius2 = 9.5
    circle1 = Circle(sample_radius1)
    circle2 = Circle(sample_radius2)
    print(f"Area of circle with radius {sample_radius1}: {circle1.calculate_area()}")
    print(f"Area of circle with radius {sample_radius2}: {circle2.calculate_area()}")