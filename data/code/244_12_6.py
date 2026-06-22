class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    @staticmethod
    def area(base, height):
        return 0.5 * base * height

class Trapezoid:
    def __init__(self, base1, base2, height):
        self.base1 = base1
        self.base2 = base2
        self.height = height

    @staticmethod
    def area(base1, base2, height):
        return 0.5 * (base1 + base2) * height

if __name__ == '__main__':
    triangle = Triangle(3, 4)
    trapezoid = Trapezoid(5, 7, 8)
    print(Triangle.area(triangle.base, triangle.height))
    print(Trapezoid.area(trapezoid.base1, trapezoid.base2, trapezoid.height))