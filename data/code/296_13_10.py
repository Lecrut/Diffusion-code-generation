class Ratio:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def simplify(self):
        gcd = self._gcd(self.numerator, self.denominator)
        return Ratio(self.numerator // gcd, self.denominator // gcd)

    def _gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    @staticmethod
    def calculate_ratio(num1, den1, num2, den2):
        common_den = den1 * den2
        new_num1 = num1 * den2
        new_num2 = num2 * den1
        return Ratio(new_num1 - new_num2, common_den)

if __name__ == '__main__':
    ratio1 = Ratio(3, 4)
    simplified_ratio = ratio1.simplify()
    print(f"Simplified Ratio: {simplified_ratio.numerator}/{simplified_ratio.denominator}")

    ratio2 = Ratio.calculate_ratio(1, 2, 3, 4)
    print(f"Ratio between 1/2 and 3/4: {ratio2.numerator}/{ratio2.denominator}")