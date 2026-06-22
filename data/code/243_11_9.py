import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
    def area(self):
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    circle_instance = Circle(5.0)
    print(f"Circle Perimeter: {circle_instance.perimeter()}")
    print(f"Circle Area: {circle_instance.area()}")