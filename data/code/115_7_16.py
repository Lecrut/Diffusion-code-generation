class Rational:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def gcd(self, a, b):
        while b:
            a, b = (b, a % b)
        return a

    def simplify(self):
        common_divisor = self.gcd(self.numerator, self.denominator)
        return (self.numerator // common_divisor, self.denominator // common_divisor)

    def __truediv__(self, other):
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Rational(new_numerator, new_denominator).simplify()
if __name__ == '__main__':
    r1 = Rational(3, 4)
    r2 = Rational(2, 5)
    result = r1 / r2
    print(result)