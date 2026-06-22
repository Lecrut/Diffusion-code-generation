from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

class CurrencyConverter:
    def __init__(self):
        self.zero = Decimal('0')

    def dollars_to_cents(self, dollars):
        if not isinstance(dollars, Decimal):
            try:
                dollars = Decimal(str(dollars))
            except (InvalidOperation, ValueError, TypeError):
                raise ValueError("Invalid currency amount")
        if dollars < self.zero:
            raise ValueError("Currency amount cannot be negative")
        cents = (dollars * Decimal('100')).quantize(
            Decimal('1'), rounding=ROUND_HALF_UP
        )
        return int(cents)

if __name__ == '__main__':
    converter = CurrencyConverter()
    sample_dollars = Decimal('12.345')
    result = converter.dollars_to_cents(sample_dollars)
    print(result)