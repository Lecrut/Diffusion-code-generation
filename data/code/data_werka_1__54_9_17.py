import math

class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    sample_radii = [1.5, 3.0, 6.2]
    for r in sample_radii:
        circle = Circle(r)
        print(f"The area of a circle with radius {r} is: {circle.area()}")