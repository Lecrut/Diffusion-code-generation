class Circle:
    def __init__(self, radius):
        self.radius = radius
    def perimeter(self):
        import math
        return 2 * math.pi * self.radius
    def area(self):
        import math
        return math.pi * self.radius ** 2
if __name__ == '__main__':
    circle1 = Circle(5)
    print(f"Circle 1 Perimeter: {circle1.perimeter()}")
    print(f"Circle 1 Area: {circle1.area()}")
    circle2 = Circle(10)
    print(f"Circle 2 Perimeter: {circle2.perimeter()}")
    print(f"Circle 2 Area: {circle2.area()}")