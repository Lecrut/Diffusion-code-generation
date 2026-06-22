import decimal

class CurrencyConverter:
    def __init__(self):
        self.quantize_value = decimal.Decimal('0.01')

    def dollars_to_cents(self, dollars):
        if not isinstance(dollars, (int, float, str, decimal.Decimal)):
            raise TypeError("Input must be a number or numeric string")
        dollar_amount = decimal.Decimal(str(dollars))
        if dollar_amount < 0:
            raise ValueError("Amount cannot be negative")
        cents_amount = dollar_amount * decimal.Decimal('100')
        return cents_amount.quantize(self.quantize_value)

if __name__ == '__main__':
    converter = CurrencyConverter()
    sample_dollars = 123.45
    result = converter.dollars_to_cents(sample_dollars)
    print(result)