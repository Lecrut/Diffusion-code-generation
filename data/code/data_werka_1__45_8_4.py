import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return self._calculate_area()
    
    def _calculate_area(self):
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    circle1 = Circle(5)
    print("Area of circle with radius 5:", circle1.area())
    
    circle2 = Circle(7)
    print("Area of circle with radius 7:", circle2.area())