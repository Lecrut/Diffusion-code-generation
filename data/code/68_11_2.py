from decimal import Decimal, ROUND_HALF_UP

class CurrencyConverter:
    def __init__(self):
        self.cent_scale = Decimal("100")

    def dollars_to_cents(self, dollar_amount):
        if isinstance(dollar_amount, float):
            dollar_amount = Decimal(str(dollar_amount))
        elif not isinstance(dollar_amount, Decimal):
            dollar_amount = Decimal(dollar_amount)
        
        cents = dollar_amount * self.cent_scale
        return cents.quantize(Decimal("1"), rounding=ROUND_HALF_UP)

if __name__ == '__main__':
    converter = CurrencyConverter()
    
    test_amounts = [
        Decimal("1"),
        Decimal("0.5"),
        Decimal("1.25"),
        Decimal("1.005"),
        Decimal("1.004"),
        Decimal("123.456"),
        Decimal("0.01"),
        Decimal("99.99"),
        Decimal("100.00"),
        Decimal("0"),
        Decimal("-1.50"),
    ]
    
    for amount in test_amounts:
        cents = converter.dollars_to_cents(amount)
        print(f"{amount} dollars = {cents} cents")