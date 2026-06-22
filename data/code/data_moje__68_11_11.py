from decimal import Decimal, InvalidOperation

class CurrencyConverter:
    def __init__(self, amount, from_currency, to_currency):
        self.amount = Decimal(str(amount))
        self.from_currency = from_currency
        self.to_currency = to_currency

    def convert(self):
        if self.from_currency == 'USD' and self.to_currency == 'USD':
            return self.amount
        if self.from_currency == 'USD' and self.to_currency == 'cents':
            return self.amount * Decimal('100')
        raise ValueError('Unsupported currency conversion')

if __name__ == '__main__':
    converter = CurrencyConverter(10.50, 'USD', 'cents')
    result = converter.convert()
    print(result)