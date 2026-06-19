import math

class Circle:
    PI = math.pi

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.PI * self.radius ** 2
if __name__ == '__main__':
    sample_radii = [2.0, 4.5, 6.3, 8.7]
    circles = [Circle(r) for r in sample_radii]
    for circle in circles:
        print(f'The area of a circle with radius {circle.radius} is: {circle.area()}')