import math

class CircleGeometry:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def diameter(self):
        return 2 * self.radius
    
    def circumference(self):
        return 2 * math.pi * self.radius

if __name__ == '__main__':
    circle = CircleGeometry(5.0)
    print("Area of the circle:", circle.area())
    print("Diameter of the circle:", circle.diameter())
    print("Circumference of the circle:", circle.circumference())