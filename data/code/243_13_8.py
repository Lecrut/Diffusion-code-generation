import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def perimeter(self):
        return 2 * math.pi * self.radius

if __name__ == '__main__':
    circle = Circle(10.5)
    print(circle.perimeter())