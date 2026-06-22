from decimal import Decimal, ROUND_DOWN

class CurrencyConverter:
    def __init__(self, dollars, cents=0):
        self.dollars = Decimal(str(dollars))
        self.cents = Decimal(str(cents))
    
    def to_total_cents(self):
        dollar_in_cents = self.dollars * 100
        total = dollar_in_cents + self.cents
        return total.quantize(Decimal('1'), rounding=ROUND_DOWN)

if __name__ == '__main__':
    sample_dollars = 123.45
    sample_cents = 50
    converter = CurrencyConverter(sample_dollars, sample_cents)
    print(converter.to_total_cents())