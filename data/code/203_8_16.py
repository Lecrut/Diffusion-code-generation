from decimal import Decimal

class DecimalComparator:
    def compare(self, d1: Decimal, d2: Decimal) -> bool:
        return d1 == d2

if __name__ == '__main__':
    comparator = DecimalComparator()
    sample_decimal1 = Decimal('0.1')
    sample_decimal2 = Decimal('0.10')
    result = comparator.compare(sample_decimal1, sample_decimal2)
    print(f"Comparing {sample_decimal1} and {sample_decimal2}: Result is {result}")
    
    another_sample_decimal1 = Decimal('123456789012345678901234567890')
    another_sample_decimal2 = Decimal('123456789012345678901234567890.0')
    result2 = comparator.compare(another_sample_decimal1, another_sample_decimal2)
    print(f"Comparing {another_sample_decimal1} and {another_sample_decimal2}: Result is {result2}")