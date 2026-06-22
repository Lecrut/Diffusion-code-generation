class Ratio:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    @staticmethod
    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def simplify(self):
        common_divisor = Ratio.gcd(self.numerator, self.denominator)
        return (self.numerator // common_divisor, self.denominator // common_divisor)

    @staticmethod
    def calculate_ratio(num1, den1, num2, den2):
        simplified1 = Ratio(num1, den1).simplify()
        simplified2 = Ratio(num2, den2).simplify()
        return (simplified1[0] * simplified2[1], simplified1[1] * simplified2[0])
if __name__ == '__main__':
    ratio1 = Ratio(4, 8)
    print(ratio1.simplify())
    result = Ratio.calculate_ratio(3, 6, 9, 12)
    print(result)