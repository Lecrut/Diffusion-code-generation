class DiscountCalculator:
    THRESHOLD = 100
    HIGH_RATE = 0.90
    LOW_RATE = 0.95

    def compute(self, price: float) -> float:
        if price > self.THRESHOLD:
            return price * self.HIGH_RATE
        return price * self.LOW_RATE

if __name__ == '__main__':
    calc = DiscountCalculator()
    print(calc.compute(50))
    print(calc.compute(150))