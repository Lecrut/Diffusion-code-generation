import math

class PowerCalculator:
    DEFAULT_BASE = 2.0
    DEFAULT_EXPONENT = 5.0

    @staticmethod
    def calculate(base, exponent):
        return math.pow(base, exponent)

if __name__ == '__main__':
    result = PowerCalculator.calculate(PowerCalculator.DEFAULT_BASE, PowerCalculator.DEFAULT_EXPONENT)
    print(result)