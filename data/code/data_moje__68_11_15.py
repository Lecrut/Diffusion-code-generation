from decimal import Decimal, ROUND_HALF_UP

class CurrencyConverter:
    def __init__(self, amount, currency_from, currency_to):
        self.amount = Decimal(str(amount))
        self.currency_from = currency_from
        self.currency_to = currency_to

    def convert(self):
        if self.currency_from == "USD" and self.currency_to == "cents":
            return (self.amount * 100).to_integral_value(rounding=ROUND_HALF_UP)
        raise ValueError("Unsupported conversion")

if __name__ == '__main__':
    converter = CurrencyConverter(10.50, "USD", "cents")
    result = converter.convert()
    print(result)