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
        common_den = den1 * den2
        new_num1 = num1 * den2
        new_num2 = num2 * den1
        return Ratio(new_num1, common_den).simplify()
if __name__ == '__main__':
    ratio1 = Ratio(4, 8)
    print(ratio1.simplify())
    result_ratio = Ratio.calculate_ratio(3, 5, 6, 9)
    print(result_ratio)