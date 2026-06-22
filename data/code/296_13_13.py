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
    def calculate_ratio(num1, num2):
        return Ratio(num1, num2).simplify()

if __name__ == '__main__':
    ratio1 = Ratio(4, 8)
    simplified_ratio1 = ratio1.simplify()
    print(f"Simplified ratio of {ratio1.numerator}/{ratio1.denominator} is {simplified_ratio1.numerator}/{simplified_ratio1.denominator}")

    result = Ratio.calculate_ratio(20, 30)
    print(f"Ratio between 20 and 30 is {result.numerator}/{result.denominator}")