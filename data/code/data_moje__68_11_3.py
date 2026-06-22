import decimal

class CurrencyConverter:
    def __init__(self):
        self.decimal_context = decimal.Context(prec=20, rounding=decimal.ROUND_HALF_UP)
        decimal.setcontext(self.decimal_context)

    def dollars_to_cents(self, dollars: str) -> int:
        dollar_value = decimal.Decimal(dollars)
        cents_value = dollar_value * 100
        return int(cents_value.to_integral_value())

if __name__ == '__main__':
    converter = CurrencyConverter()
    sample_dollars = "123.45"
    result = converter.dollars_to_cents(sample_dollars)
    print(result)