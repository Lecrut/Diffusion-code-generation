import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius ** 2)
    
    def perimeter(self):
        return 2 * math.pi * self.radius

class Triangle:
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def area(self):
        return 0.5 * self.base * self.height
    
    def perimeter(self):
        return self.side1 + self.side2 + self.side3

if __name__ == '__main__':
    circle = Circle(radius=5)
    print("Circle Area:", circle.area())
    print("Circle Perimeter:", circle.perimeter())

    triangle = Triangle(base=10, height=4, side1=6, side2=8, side3=10)
    print("Triangle Area:", triangle.area())
    print("Triangle Perimeter:", triangle.perimeter())