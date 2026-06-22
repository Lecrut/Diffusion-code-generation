import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius ** 2)
    
    def perimeter(self):
        return 2 * math.pi * self.radius

class Triangle:
    def __init__(self, base, height, side1=None, side2=None, side3=None):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def area(self):
        return 0.5 * self.base * self.height
    
    def perimeter(self):
        if self.side1 is not None and self.side2 is not None and self.side3 is not None:
            return self.side1 + self.side2 + self.side3
        else:
            raise ValueError("All three sides must be provided to calculate the perimeter of a triangle.")

if __name__ == '__main__':
    circle = Circle(radius=5)
    print(f"Circle Area: {circle.area()}")
    print(f"Circle Perimeter: {circle.perimeter()}")

    triangle = Triangle(base=4, height=6, side1=3, side2=4, side3=5)
    print(f"Triangle Area: {triangle.area()}")
    print(f"Triangle Perimeter: {triangle.perimeter()}")