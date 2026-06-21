import decimal

class DecimalComparator:
    @staticmethod
    def are_equal(d1, d2):
        return d1 == d2

if __name__ == '__main__':
    dec_a = decimal.Decimal('0.1')
    dec_b = decimal.Decimal('0.1')
    result = DecimalComparator.are_equal(dec_a, dec_b)
    print(f"Comparing {dec_a} and {dec_b}: {'Equal' if result else 'Not Equal'}")