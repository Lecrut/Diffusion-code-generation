class RationalNumber:

    def __init__(self, numerator=0, denominator=1):
        gcd = self._gcd(numerator, denominator)
        self.numerator = numerator // gcd
        self.denominator = denominator // gcd

    def _gcd(self, a, b):
        while b != 0:
            a, b = (b, a % b)
        return a

    def __truediv__(self, other):
        if isinstance(other, RationalNumber):
            new_numerator = self.numerator * other.denominator
            new_denominator = self.denominator * other.numerator
        else:
            raise ValueError('Cannot divide by non-RationalNumber')
        return RationalNumber(new_numerator, new_denominator)

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'
if __name__ == '__main__':
    r1 = RationalNumber(3, 4)
    r2 = RationalNumber(2, 5)
    print(r1 / r2)