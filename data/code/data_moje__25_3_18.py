class DiscountCalculator:
    HIGH_TIER_THRESHOLD = 100
    HIGH_TIER_RATE = 0.90
    LOW_TIER_RATE = 0.95

    def calculate(self, price):
        if price > self.HIGH_TIER_THRESHOLD:
            return price * self.HIGH_TIER_RATE
        return price * self.LOW_TIER_RATE

if __name__ == '__main__':
    calculator = DiscountCalculator()
    print(calculator.calculate(50))
    print(calculator.calculate(150))