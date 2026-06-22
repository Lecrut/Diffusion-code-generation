class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Trapezoid:
    def __init__(self, base1, base2, height):
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def area(self):
        return 0.5 * (self.base1 + self.base2) * self.height

if __name__ == '__main__':
    triangle = Triangle(4, 6)
    trapezoid = Trapezoid(7, 9, 5)
    total_area = triangle.area() + trapezoid.area()
    print(f"Total area: {total_area}")