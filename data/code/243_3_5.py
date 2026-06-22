import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def perimeter(self):
        return 2 * math.pi * self.radius

if __name__ == '__main__':
    circle1 = Circle(10)
    print(circle1.perimeter())
    circle2 = Circle(5)
    print(circle2.perimeter())