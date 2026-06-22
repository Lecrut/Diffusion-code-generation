class PricingEngine:
    def __init__(self, base_price):
        self.base_price = base_price

    def calculate_discounted_price(self):
        if self.base_price > 100:
            return self.base_price * 0.9
        return self.base_price * 0.95

if __name__ == '__main__':
    engine_low = PricingEngine(50)
    engine_high = PricingEngine(150)
    print(engine_low.calculate_discounted_price())
    print(engine_high.calculate_discounted_price())