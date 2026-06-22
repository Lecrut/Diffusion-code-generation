class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def get_area(self):
        return 0.5 * self.base * self.height

    def get_perimeter_approx(self):
        return self.base + self.height * 2

if __name__ == '__main__':
    tri = Triangle(8, 6)
    print(tri.get_area())
    print(tri.get_perimeter_approx())