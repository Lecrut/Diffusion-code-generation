import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return self._calculate_area()
    
    def _calculate_area(self):
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    circle = Circle(7)
    print(circle.area())