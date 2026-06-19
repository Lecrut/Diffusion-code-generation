import math

class CircleGeometry:
    def __init__(self, radius):
        self.radius = radius
    
    def compute_area(self):
        return math.pi * self.radius ** 2
    
    def compute_diameter(self):
        return 2 * self.radius

if __name__ == '__main__':
    circle_geometry = CircleGeometry(5.0)
    area = circle_geometry.compute_area()
    diameter = circle_geometry.compute_diameter()
    print("Area of the circle:", area)
    print("Diameter of the circle:", diameter)