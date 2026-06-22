from decimal import Decimal

class CurrencyConverter:
    def __init__(self):
        self.dollars_to_cents_factor = Decimal('100')

    def convert_to_cents(self, dollar_amount):
        dollar_decimal = Decimal(str(dollar_amount))
        return int(dollar_decimal * self.dollars_to_cents_factor)

if __name__ == '__main__':
    converter = CurrencyConverter()
    amount_dollars = 12.50
    cents = converter.convert_to_cents(amount_dollars)
    print(cents)