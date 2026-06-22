import math

class Ratio:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def simplify(self):
        common_divisor = math.gcd(self.numerator, self.denominator)
        self.numerator //= common_divisor
        self.denominator //= common_divisor

if __name__ == '__main__':
    ratio1 = Ratio(10, 15)
    print(f"Initial Ratio: {ratio1.numerator}/{ratio1.denominator}")
    ratio1.simplify()
    print(f"Simplified Ratio: {ratio1.numerator}/{ratio1.denominator}")

    ratio2 = Ratio(20, 7)
    print(f"\nInitial Ratio: {ratio2.numerator}/{ratio2.denominator}")
    ratio2.simplify()
    print(f"Simplified Ratio: {ratio2.numerator}/{ratio2.denominator}")