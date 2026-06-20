from decimal import Decimal

class PrecisionComparator:
    TOLERANCE = Decimal('1e-28')

    @staticmethod
    def are_equal(a: Decimal, b: Decimal) -> bool:
        return abs(a - b) <= PrecisionComparator.TOLERANCE

    @staticmethod
    def are_not_equal(a: Decimal, b: Decimal) -> bool:
        return not PrecisionComparator.are_equal(a, b)
if __name__ == '__main__':
    value1 = Decimal('0.12345678901234567890123456789')
    value2 = Decimal('0.12345678901234567890123456788')
    print('Are values equal?', PrecisionComparator.are_equal(value1, value2))
    print('Are values not equal?', PrecisionComparator.are_not_equal(value1, value2))