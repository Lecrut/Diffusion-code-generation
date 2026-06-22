import decimal

class CurrencyConverter:
    def __init__(self):
        self.decimal_context = decimal.getcontext()

    def dollars_to_cents(self, amount_dollars):
        amount_decimal = decimal.Decimal(str(amount_dollars))
        multiplier = decimal.Decimal('100')
        result = amount_decimal * multiplier
        return result

if __name__ == '__main__':
    converter = CurrencyConverter()
    sample_dollars = 123.45
    converted_cents = converter.dollars_to_cents(sample_dollars)
    print(converted_cents)
    sample_dollars_2 = 0.01
    converted_cents_2 = converter.dollars_to_cents(sample_dollars_2)
    print(converted_cents_2)
    sample_dollars_3 = 1000
    converted_cents_3 = converter.dollars_to_cents(sample_dollars_3)
    print(converted_cents_3)