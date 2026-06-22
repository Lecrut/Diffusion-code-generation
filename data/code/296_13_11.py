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
        ratio1 = Ratio(num1, den1).simplify()
        ratio2 = Ratio(num2, den2).simplify()
        if ratio1 == ratio2:
            return True
        else:
            return False
if __name__ == '__main__':
    r1 = Ratio(4, 8)
    print(r1.simplify())
    print(Ratio.calculate_ratio(3, 6, 9, 18))