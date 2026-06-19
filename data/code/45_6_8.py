import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2

if __name__ == '__main__':
    circle1 = Circle(1)
    print(circle1.area())
    
    circle2 = Circle(2.5)
    print(circle2.area())
    
    circle3 = Circle(0)
    print(circle3.area())
    
    circle4 = Circle(10)
    print(circle4.area())