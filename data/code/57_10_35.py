import math

def compute_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * (radius ** 2)

class CircleGeometry:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return compute_circle_area(self.radius)
    
    def circumference(self):
        return 2 * math.pi * self.radius

if __name__ == '__main__':
    sample_radius = 5
    circle_geometry_instance = CircleGeometry(sample_radius)
    print("Area:", circle_geometry_instance.area())
    print("Circumference:", circle_geometry_instance.circumference())