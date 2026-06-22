from decimal import Decimal, ROUND_HALF_UP

class CurrencyConverter:
    def __init__(self):
        self.cent_multiplier = Decimal('100')

    def dollars_to_cents(self, dollars):
        if not isinstance(dollars, Decimal):
            dollars = Decimal(str(dollars))
        cents = (dollars * self.cent_multiplier).quantize(
            Decimal('1'), rounding=ROUND_HALF_UP
        )
        return cents

if __name__ == '__main__':
    converter = CurrencyConverter()
    sample_dollars = Decimal('123.456')
    result_cents = converter.dollars_to_cents(sample_dollars)
    print(result_cents)