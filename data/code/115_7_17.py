class RationalNumber:

    def __init__(self, numerator, denominator):
        gcd = self._gcd(numerator, denominator)
        self.numerator = numerator // gcd
        self.denominator = denominator // gcd

    def _gcd(self, a, b):
        while b:
            a, b = (b, a % b)
        return a

    def __truediv__(self, other):
        if isinstance(other, RationalNumber):
            new_numerator = self.numerator * other.denominator
            new_denominator = self.denominator * other.numerator
            gcd = self._gcd(new_numerator, new_denominator)
            return (new_numerator // gcd, new_denominator // gcd)
        else:
            raise TypeError("Unsupported operand type for /: 'RationalNumber' and '{}'".format(type(other).__name__))
if __name__ == '__main__':
    r1 = RationalNumber(10, 2)
    r2 = RationalNumber(5, 3)
    result = r1 / r2
    print(result)
    r3 = RationalNumber(-10, 5)
    r4 = RationalNumber(2, -3)
    result = r3 / r4
    print(result)
    r5 = RationalNumber(0, 7)
    r6 = RationalNumber(8, 2)
    result = r5 / r6
    print(result)