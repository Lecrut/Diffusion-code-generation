class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    triangle = Triangle(20, 10)
    print(triangle.area())
    print(f"Base: {triangle.base}, Height: {triangle.height}")