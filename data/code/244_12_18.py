class Triangle:
    def __init__(self, base: float, height: float):
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive numbers")
        self.base = base
        self.height = height

    def area(self) -> float:
        return 0.5 * self.base * self.height

class Trapezoid:
    def __init__(self, base1: float, base2: float, height: float):
        if base1 <= 0 or base2 <= 0 or height <= 0:
            raise ValueError("All dimensions must be positive numbers")
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def area(self) -> float:
        return 0.5 * (self.base1 + self.base2) * self.height

if __name__ == '__main__':
    triangle = Triangle(3, 4)
    trapezoid = Trapezoid(5, 7, 8)
    print("Triangle area:", triangle.area())
    print("Trapezoid area:", trapezoid.area())