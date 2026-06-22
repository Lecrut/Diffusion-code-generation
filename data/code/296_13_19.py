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
    def calculate_ratio(num1, num2):
        numerator = abs(num1 * 100 - num2 * 100)
        denominator = max(abs(num1), abs(num2))
        gcd = Ratio._gcd(numerator, denominator)
        return (numerator // gcd, denominator // gcd)
if __name__ == '__main__':
    ratio = Ratio(45, 90)
    print(ratio.simplify())
    print(Ratio.calculate_ratio(3, 6))