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
        ratio1 = Ratio(num1, den1).simplify()
        ratio2 = Ratio(num2, den2).simplify()
        if ratio1.numerator * ratio2.denominator == ratio1.denominator * ratio2.numerator:
            return "Equal"
        elif ratio1.numerator * ratio2.denominator > ratio1.denominator * ratio2.numerator:
            return "Greater"
        else:
            return "Less"

if __name__ == '__main__':
    sample_ratio = Ratio(4, 8)
    simplified_ratio = sample_ratio.simplify()
    print(f"Simplified Ratio: {simplified_ratio.numerator}/{simplified_ratio.denominator}")

    result = Ratio.calculate_ratio(2, 3, 4, 6)
    print(f"Ratio Comparison: {result}")