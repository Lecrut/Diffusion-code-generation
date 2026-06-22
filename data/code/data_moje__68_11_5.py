from decimal import Decimal, getcontext, ROUND_HALF_UP

getcontext().prec = 10

class CurrencyConverter:
    def __init__(self, rate):
        self.rate = Decimal(str(rate))

    def dollars_to_cents(self, dollars):
        cents = Decimal(str(dollars)) * Decimal("100")
        return int(cents.quantize(Decimal("1"), rounding=ROUND_HALF_UP))

if __name__ == '__main__':
    converter = CurrencyConverter(1.0)
    amount_in_dollars = 42.50
    result = converter.dollars_to_cents(amount_in_dollars)
    print(result)