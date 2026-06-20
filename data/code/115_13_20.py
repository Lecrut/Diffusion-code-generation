from decimal import Decimal, getcontext

class PrecisionDivider:
    def __init__(self):
        getcontext().prec = 50

    def divide(self, a, b):
        return a / b

if __name__ == '__main__':
    divider = PrecisionDivider()
    result1 = divider.divide(Decimal('1.0'), Decimal('3.0'))
    result2 = divider.divide(Decimal('1.234567890123456789012345678901234567890123456789'), Decimal('2.345678901234567890123456789012345678901234567890'))
    print(result1)
    print(result2)