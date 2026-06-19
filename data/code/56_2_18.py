import math

class Circle:
    PI = math.pi
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return self.PI * (self.radius ** 2)
    
    def perimeter(self):
        return 2 * self.PI * self.radius

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
    circle = Circle(radius=7)
    print("Circle Area:", circle.area())
    print("Circle Perimeter:", circle.perimeter())

    triangle = Triangle(base=5, height=8, side1=6, side2=7, side3=9)
    print("Triangle Area:", triangle.area())
    print("Triangle Perimeter:", triangle.perimeter())