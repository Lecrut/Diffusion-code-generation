from decimal import Decimal

class CurrencyConverter:
    def __init__(self, dollars: str):
        self.dollars = Decimal(dollars)

    def to_cents(self) -> Decimal:
        return self.dollars * 100

if __name__ == '__main__':
    sample_dollars = "1234.56"
    converter = CurrencyConverter(sample_dollars)
    result = converter.to_cents()
    print(result)