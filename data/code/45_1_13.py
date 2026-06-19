import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius ** 2)
    
    def diameter(self):
        return 2 * self.radius

if __name__ == '__main__':
    circle1 = Circle(5.0)
    print("Area of circle with radius 5.0:", circle1.area())
    print("Diameter of circle with radius 5.0:", circle1.diameter())

    circle2 = Circle(10.0)
    print("Area of circle with radius 10.0:", circle2.area())
    print("Diameter of circle with radius 10.0:", circle2.diameter())