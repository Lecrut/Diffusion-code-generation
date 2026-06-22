class Ratio:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def simplify(self):
        gcd = self._gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

    def add(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Ratio(new_numerator, new_denominator)

    def _gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

if __name__ == '__main__':
    ratio1 = Ratio(3, 4)
    ratio2 = Ratio(1, 2)
    result_ratio = ratio1.add(ratio2)
    result_ratio.simplify()
    print(f"{result_ratio.numerator}/{result_ratio.denominator}")