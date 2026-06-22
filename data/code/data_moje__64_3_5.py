import math

class PowerCalculator:
    def __init__(self, base_value):
        self.base = base_value

    def raise_to_power(self, exponent):
        return math.pow(self.base, exponent)

    def raise_to_half_power(self):
        return self.raise_to_power(0.5)

if __name__ == '__main__':
    calc = PowerCalculator(4.0)
    result1 = calc.raise_to_power(3)
    result2 = calc.raise_to_half_power()
    print(result1)
    print(result2)