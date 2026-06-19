import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    sample_radii = [1.5, 3.2, 6.7]
    circles = [Circle(r) for r in sample_radii]
    for i, circle in enumerate(circles, start=1):
        print(f"The area of circle {i} with radius {circle.radius} is: {circle.area()}")