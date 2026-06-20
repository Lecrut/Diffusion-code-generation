from decimal import Decimal

class MonetaryCalculator:
    def __init__(self, amount_a, amount_b):
        self.amount_a = Decimal(str(amount_a))
        self.amount_b = Decimal(str(amount_b))

    def calculate_difference(self):
        return self.amount_a - self.amount_b

if __name__ == '__main__':
    calculator = MonetaryCalculator(10.50, 3.25)
    print(calculator.calculate_difference())