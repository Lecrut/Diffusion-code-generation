class RationalNumber:

    def __init__(self, numerator=0, denominator=1):
        if denominator == 0:
            raise ValueError('Denominator cannot be zero')
        self.numerator = numerator
        self.denominator = denominator

    @staticmethod
    def gcd(x, y):
        while y != 0:
            x, y = (y, x % y)
        return x

    def simplify(self):
        common_divisor = self.gcd(abs(self.numerator), abs(self.denominator))
        return (self.numerator // common_divisor, self.denominator // common_divisor)

    def __truediv__(self, other):
        if isinstance(other, RationalNumber):
            new_numerator = self.numerator * other.denominator
            new_denominator = self.denominator * other.numerator
            return RationalNumber(new_numerator, new_denominator).simplify()
        else:
            raise TypeError("Unsupported operand type(s) for /: 'RationalNumber' and '{}'".format(type(other).__name__))
if __name__ == '__main__':
    r1 = RationalNumber(4, 8)
    r2 = RationalNumber(3, 6)
    print(r1 / r2)