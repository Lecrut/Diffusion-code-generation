class Triangle:
    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height

    def area(self) -> float:
        return 0.5 * self.base * self.height

class Trapezoid:
    def __init__(self, base1: float, base2: float, height: float):
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def area(self) -> float:
        return 0.5 * (self.base1 + self.base2) * self.height

if __name__ == '__main__':
    triangle = Triangle(3, 4)
    trapezoid = Trapezoid(5, 7, 8)
    print(triangle.area())
    print(trapezoid.area())