from decimal import Decimal

class DecimalComparator:
    def are_equal(self, dec1: Decimal, dec2: Decimal) -> bool:
        return dec1 == dec2

if __name__ == '__main__':
    comparator = DecimalComparator()
    sample1 = Decimal('0.1000')
    sample2 = Decimal('0.10000')
    print(comparator.are_equal(sample1, sample2))
    print(comparator.are_equal(sample1, sample1))