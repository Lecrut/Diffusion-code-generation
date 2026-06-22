class TriangleCalculator:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter_approx(self):
        hypotenuse = (self.base ** 2 + self.height ** 2) ** 0.5
        return self.base + self.height + hypotenuse

if __name__ == '__main__':
    calc = TriangleCalculator(10, 5)
    print(calc.area())
    print(calc.perimeter_approx())