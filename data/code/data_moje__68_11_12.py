import decimal

class CurrencyConverter:
    def __init__(self, dollars):
        self.dollars = decimal.Decimal(str(dollars))
        self.scale = decimal.Decimal('100')

    def convert_to_cents(self):
        return self.dollars * self.scale

if __name__ == '__main__':
    sample_dollars = 123.45
    converter = CurrencyConverter(sample_dollars)
    cents = converter.convert_to_cents()
    print(cents)