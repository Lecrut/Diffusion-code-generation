DISCOUNT_THRESHOLD = 100
HIGH_TIER_RATE = 0.10
LOW_TIER_RATE = 0.05

class PricingEngine:
    def __init__(self, base_threshold, high_rate, low_rate):
        self.base_threshold = base_threshold
        self.high_rate = high_rate
        self.low_rate = low_rate

    def apply_discount(self, price):
        if price > self.base_threshold:
            return price * (1 - self.high_rate)
        return price * (1 - self.low_rate)

if __name__ == '__main__':
    engine = PricingEngine(DISCOUNT_THRESHOLD, HIGH_TIER_RATE, LOW_TIER_RATE)
    print(engine.apply_discount(50))
    print(engine.apply_discount(150))