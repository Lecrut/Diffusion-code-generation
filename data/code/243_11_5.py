class Circle:
    def __init__(self, radius):
        self.radius = radius
    def perimeter(self):
        return 2 * 3.14159 * self.radius
    def area(self):
        return 3.14159 * self.radius ** 2
if __name__ == '__main__':
    r = 5.0
    c = Circle(r)
    p = c.perimeter()
    a = c.area()
    print(f"Radius: {r}")
    print(f"Perimeter: {p}")
    print(f"Area: {a}")