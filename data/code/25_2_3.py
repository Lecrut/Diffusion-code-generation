DISCOUNT_RATE = 0.20

class PriceCalculator:
    def __init__(self, base_price):
        self.base_price = base_price

    def calculate(self, discount_rate):
        if not (0 <= discount_rate <= 1):
            raise ValueError("Discount rate must be between 0 and 1")
        savings = self.base_price * discount_rate
        final_price = self.base_price - savings
        return savings, final_price

if __name__ == '__main__':
    calculator = PriceCalculator(500)
    savings, final_price = calculator.calculate(DISCOUNT_RATE)
    print(savings)
    print(final_price)