import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self._calculate_area()

    def _calculate_area(self):
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    sample_radii = {'circle1': 3, 'circle2': 8}
    
    for name, radius in sample_radii.items():
        circle = Circle(radius)
        print(f"Area of {name} with radius {radius}: {circle.area()}")