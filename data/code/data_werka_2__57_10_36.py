import math

class CircleGeometry:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius
    
    def calculate_area(self):
        return math.pi * (self.radius ** 2)
    
    def calculate_circumference(self):
        return 2 * math.pi * self.radius

if __name__ == '__main__':
    sample_radius = 5
    geometry_instance = CircleGeometry(sample_radius)
    print("Area:", geometry_instance.calculate_area())
    print("Circumference:", geometry_instance.calculate_circumference())