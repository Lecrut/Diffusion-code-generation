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
        self.sides = {'side1': side1, 'side2': side2, 'side3': side3}
    
    def area(self):
        return 0.5 * self.base * self.height
    
    def perimeter(self):
        if None in self.sides.values():
            raise ValueError("All sides must be provided to calculate the perimeter.")
        return sum(self.sides.values())

if __name__ == '__main__':
    circle = Circle(radius=5)
    print(f"Circle Area: {circle.area()}")
    print(f"Circle Perimeter: {circle.perimeter()}")

    triangle = Triangle(base=10, height=4, side1=6, side2=8, side3=10)
    print(f"Triangle Area: {triangle.area()}")
    print(f"Triangle Perimeter: {triangle.perimeter()}")