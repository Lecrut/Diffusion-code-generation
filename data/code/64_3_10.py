import math

class PowerCalculator:
    def __init__(self, base_value):
        self.base = base_value

    def calculate(self, exponent):
        return math.pow(self.base, exponent)

    def scale_result(self, exponent, factor):
        return self.calculate(exponent) * factor

if __name__ == '__main__':
    calc = PowerCalculator(5.0)
    value1 = calc.calculate(2.0)
    value2 = calc.scale_result(3.0, 0.5)
    print(value1)
    print(value2)