from decimal import Decimal, ROUND_HALF_UP

class CurrencyConverter:
    def __init__(self, amount):
        self.amount = Decimal(str(amount))

    def to_cents(self):
        return (self.amount * 100).to_integral_value(rounding=ROUND_HALF_UP)

if __name__ == '__main__':
    dollar_amount = 42.50
    converter = CurrencyConverter(dollar_amount)
    result = converter.to_cents()
    print(result)