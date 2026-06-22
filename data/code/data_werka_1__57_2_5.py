class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    triangle1 = Triangle(base=8.0, height=3.0)
    print(f"Area of triangle with base 8 and height 3: {triangle1.area()}")

    triangle2 = Triangle(base=12.5, height=6.4)
    print(f"Area of triangle with base 12.5 and height 6.4: {triangle2.area()}")