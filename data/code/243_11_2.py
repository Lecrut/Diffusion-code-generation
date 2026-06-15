class Circle:
    def __init__(self, radius):
        self.radius = radius
    def perimeter(self):
        import math
        return 2 * math.pi * self.radius
    def area(self):
        import math
        return math.pi * self.radius**2
if __name__ == '__main__':
    r = 5.0
    c = Circle(r)
    print(f"Radius: {r}")
    print(f"Perimeter: {c.perimeter()}")
    print(f"Area: {c.area()}")