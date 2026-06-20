class Rational:

    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError('Denominator cannot be zero')
        self.numerator = numerator
        self.denominator = denominator

    @staticmethod
    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a

    def simplify(self):
        common_divisor = Rational.gcd(abs(self.numerator), abs(self.denominator))
        return (self.numerator // common_divisor, self.denominator // common_divisor)

    def __truediv__(self, other):
        if isinstance(other, int):
            other = Rational(0, other)
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Rational(new_numerator, new_denominator).simplify()
if __name__ == '__main__':
    r1 = Rational(10, 2)
    r2 = Rational(5, 5)
    r3 = Rational(-10, 5)
    r4 = Rational(0, 3)
    print(r1 / r2)
    print(r1 / r3)
    print(r1 / r4)