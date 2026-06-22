from decimal import Decimal, ROUND_DOWN

class CurrencyConverter:
    def __init__(self, dollars: Decimal):
        self.dollars = dollars

    def to_cents(self) -> int:
        cents_decimal = self.dollars * Decimal('100')
        return int(cents_decimal.quantize(Decimal('1'), rounding=ROUND_DOWN))

if __name__ == '__main__':
    sample_dollars = Decimal('123.45')
    converter = CurrencyConverter(sample_dollars)
    result = converter.to_cents()
    print(result)