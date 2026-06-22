import math

class EllipseCalculator:
    def __init__(self, semi_major, semi_minor):
        self.semi_major = semi_major
        self.semi_minor = semi_minor

    def area(self):
        return math.pi * self.semi_major * self.semi_minor

    def perimeter_approximation(self):
        h = ((self.semi_major - self.semi_minor) ** 2) / ((self.semi_major + self.semi_minor) ** 2)
        return math.pi * (self.semi_major + self.semi_minor) * (1 + (3 * h) / (10 + math.sqrt(4 - 3 * h)))

if __name__ == '__main__':
    calculator = EllipseCalculator(5.0, 3.0)
    print(calculator.area())
    print(calculator.perimeter_approximation())