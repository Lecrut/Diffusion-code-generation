import math

class Circle:
    def __init__(self, radius):
        self.radius = float(radius)
    
    def area(self):
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    circle1 = Circle(5.0)
    print(circle1.area())
    
    circle2 = Circle(10)
    print(circle2.area())
    
    circle3 = Circle(7.25)
    print(circle3.area())