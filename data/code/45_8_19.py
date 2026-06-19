import math

class Circle:
    def __init__(self, radius):
        self.set_radius(radius)
    
    def set_radius(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = radius
    
    def get_radius(self):
        return self._radius
    
    def area(self):
        return math.pi * (self.get_radius() ** 2)

if __name__ == '__main__':
    try:
        circle = Circle(8)
        print(f"Area of circle with radius {circle.get_radius()}:", circle.area())
    except ValueError as e:
        print(e)