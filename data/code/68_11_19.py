from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

CENT_MULTIPLIER = Decimal('100')
INTEGER_QUANTIZE = Decimal('1')

class CurrencyConverter:
    def __init__(self):
        self.multiplier = CENT_MULTIPLIER
        self.quantizer = INTEGER_QUANTIZE

    def convert_to_cents(self, amount):
        if not isinstance(amount, (int, float, str, Decimal)):
            raise TypeError("Amount must be numeric")
        try:
            decimal_amount = Decimal(str(amount))
        except (InvalidOperation, ValueError):
            raise ValueError("Invalid numeric format")
        if decimal_amount < 0:
            raise ValueError("Amount cannot be negative")
        cents = decimal_amount * self.multiplier
        return int(cents.quantize(self.quantizer, rounding=ROUND_HALF_UP))

if __name__ == '__main__':
    converter = CurrencyConverter()
    sample_value = Decimal('12.99')
    converted_cents = converter.convert_to_cents(sample_value)
    print(converted_cents)