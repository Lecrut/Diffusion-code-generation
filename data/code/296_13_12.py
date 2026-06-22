class Ratio:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def simplify(self):
        gcd = self._gcd(self.numerator, self.denominator)
        return (self.numerator // gcd, self.denominator // gcd)

    def _gcd(self, a, b):
        while b:
            a, b = (b, a % b)
        return a

    @staticmethod
    def calculate_ratio(num1, den1, num2, den2):
        numerator = num1 * den2 - num2 * den1
        denominator = den1 * den2
        gcd = Ratio._gcd(numerator, denominator)
        return (numerator // gcd, denominator // gcd)
if __name__ == '__main__':
    ratio1 = Ratio(98, 42)
    print(ratio1.simplify())
    ratio2 = Ratio.calculate_ratio(1, 2, 3, 4)
    print(ratio2)