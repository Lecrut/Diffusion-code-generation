from decimal import Decimal

class PreciseDivider:

    def __init__(self):
        self.precision = 100

    @staticmethod
    def _to_decimal(value):
        return Decimal(str(value)).quantize(Decimal('0.' + '0' * 98))

    def divide(self, dividend, divisor):
        if divisor == 0:
            raise ZeroDivisionError('Divisor cannot be zero')
        dec_dividend = self._to_decimal(dividend)
        dec_divisor = self._to_decimal(divisor)
        return dec_dividend / dec_divisor
if __name__ == '__main__':
    divider = PreciseDivider()
    result = divider.divide(10, 3)
    print(result)
    result = divider.divide(10, 2)
    print(result)
    result = divider.divide(7, 2)
    print(result)