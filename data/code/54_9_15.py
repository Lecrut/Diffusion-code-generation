import math

class Circle:
    PI = math.pi

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.PI * self.radius ** 2
if __name__ == '__main__':
    sample_values = [1.0, 3.5, 8.2, 12.7]
    for radius in sample_values:
        circle = Circle(radius)
        print(f'The area of a circle with radius {radius} is: {circle.area()}')