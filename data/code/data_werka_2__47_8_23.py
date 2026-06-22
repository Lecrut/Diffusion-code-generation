class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    triangle1 = Triangle(10, 5)
    print(f"Area of triangle1: {triangle1.area()}")

    triangle2 = Triangle(8, 6)
    print(f"Area of triangle2: {triangle2.area()}")