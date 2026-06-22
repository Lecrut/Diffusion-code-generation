class DiscountCalculator:
    PRICE_TIER_THRESHOLDS = (0, 50, 100, 200, 500)
    DISCOUNT_RATES = (0.0, 0.05, 0.10, 0.15, 0.20)

    @staticmethod
    def calculate_discount(price):
        if price < 0:
            return 0.0
        for i in range(len(DiscountCalculator.PRICE_TIER_THRESHOLDS) - 1, 0, -1):
            if price >= DiscountCalculator.PRICE_TIER_THRESHOLDS[i]:
                return price * DiscountCalculator.DISCOUNT_RATES[i]
        return price * DiscountCalculator.DISCOUNT_RATES[0]

if __name__ == '__main__':
    calculator = DiscountCalculator()
    sample_prices = [0, 25, 75, 150, 300, 600]
    for p in sample_prices:
        discount = calculator.calculate_discount(p)
        print(f"Price: {p}, Discount: {discount}")