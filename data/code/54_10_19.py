import math

class Circle:
    PI = math.pi
    
    def __init__(self, radius):
        self.radius = radius
    
    @staticmethod
    def area(radius):
        return Circle.PI * radius ** 2

if __name__ == '__main__':
    circle = Circle(10)
    print(Circle.area(circle.radius))