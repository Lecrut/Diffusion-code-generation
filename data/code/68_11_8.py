from decimal import Decimal, ROUND_HALF_UP

class DollarToCentConverter:
    def __init__(self):
        self.conversion_rate = Decimal('100')

    def convert(self, dollars):
        if not isinstance(dollars, (int, float, Decimal)):
            raise TypeError("Input must be a number")
        dollars_decimal = Decimal(str(dollars))
        cents = dollars_decimal * self.conversion_rate
        return cents.quantize(Decimal('1'), rounding=ROUND_HALF_UP)

if __name__ == '__main__':
    converter = DollarToCentConverter()
    sample_dollars = 12.345
    result = converter.convert(sample_dollars)
    print(result)