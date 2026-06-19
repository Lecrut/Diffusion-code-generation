import math

class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    sample_radii = [1.5, 3.2, 7.8]
    circles = [Circle(r) for r in sample_radii]
    for circle in circles:
        print(f"The area of a circle with radius {circle.radius} is: {circle.area()}")