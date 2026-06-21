class TieredPricingEngine:
    def __init__(self, threshold=100, high_discount=0.10, low_discount=0.05):
        self.threshold = threshold
        self.high_discount = high_discount
        self.low_discount = low_discount

    def apply(self, price):
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a number")
        if price < 0:
            raise ValueError("Price cannot be negative")
        if price > self.threshold:
            return price * (1 - self.high_discount)
        return price * (1 - self.low_discount)

if __name__ == '__main__':
    engine = TieredPricingEngine()
    print(engine.apply(50))
    print(engine.apply(150))