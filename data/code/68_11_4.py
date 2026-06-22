import decimal

class CurrencyConverter:
    def __init__(self):
        self.context = decimal.getcontext()
        self.context.prec = 10

    def dollars_to_cents(self, dollars):
        dollar_amount = decimal.Decimal(str(dolars))
        cent_amount = dollar_amount * decimal.Decimal('100')
        return cent_amount

if __name__ == '__main__':
    dollars = 123.45
    converter = CurrencyConverter()
    cents = converter.dollars_to_cents(dollars)
    print(cents)