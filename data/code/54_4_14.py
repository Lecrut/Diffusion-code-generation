import math

class Circle:
    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = self._calculate_radius()
    
    def _calculate_radius(self):
        return self.diameter / 2
    
    def area(self):
        return math.pi * (self.radius ** 2)

def area_from_diameter(diameter):
    circle = Circle(diameter)
    return circle.area()

if __name__ == '__main__':
    sample_diameters = [10, 25.4, 0, -3]
    for diameter in sample_diameters:
        try:
            print(f"Area of circle with diameter {diameter}: {area_from_diameter(diameter)}")
        except ValueError as e:
            print(e)