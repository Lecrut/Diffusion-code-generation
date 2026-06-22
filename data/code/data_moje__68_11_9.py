from decimal import Decimal, InvalidOperation

class CurrencyConverter:
    def __init__(self, exchange_rate=Decimal('100')):
        self.exchange_rate = Decimal(exchange_rate)

    def dollars_to_cents(self, amount_dollars):
        amount_decimal = Decimal(str(amount_dollars))
        if amount_decimal < 0:
            return Decimal('0')
        return amount_decimal * self.exchange_rate

if __name__ == '__main__':
    converter = CurrencyConverter()
    dollars_amount = Decimal('12.34')
    result = converter.dollars_to_cents(dollars_amount)
    print(result)