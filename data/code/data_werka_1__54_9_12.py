import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    sample_radii = [1.5, 3.0, 6.7, 9.2]
    for radius in sample_radii:
        circle = Circle(radius)
        print(f"The area of a circle with radius {radius} is: {circle.area()}")