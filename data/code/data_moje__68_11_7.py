import decimal

class CurrencyConverter:
    def __init__(self):
        self.set_quantum(100)

    def set_quantum(self, value):
        self.quantum = decimal.Decimal(value)

    def to_cents(self, dollars):
        return int(decimal.Decimal(str(dollars)) * self.quantum)

if __name__ == '__main__':
    converter = CurrencyConverter()
    amount = 123.45
    result = converter.to_cents(amount)
    print(result)