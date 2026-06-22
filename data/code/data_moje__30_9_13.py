import math

class CircleCalculator:
    def __init__(self, pi_value=None):
        self.pi = pi_value if pi_value is not None else math.pi

    def get_area(self, radius):
        return self.pi * (radius ** 2)

    def get_circumference(self, radius):
        return 2 * self.pi * radius

if __name__ == '__main__':
    calc = CircleCalculator()
    r = 3
    print(calc.get_area(r))
    print(calc.get_circumference(r))