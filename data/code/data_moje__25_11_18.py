class TieredDiscountCalculator:
    BASE_PRICE = 1000.0
    TIER_RANGES = [
        (100, 0.25),
        (50, 0.15),
        (20, 0.08),
        (0, 0.0)
    ]

    @staticmethod
    def calculate_final_price(quantity):
        if quantity < 0:
            return 0.0
        total_cost = quantity * TieredDiscountCalculator.BASE_PRICE
        for min_qty, discount_rate in TieredDiscountCalculator.TIER_RANGES:
            if quantity >= min_qty:
                discount_amount = total_cost * discount_rate
                return total_cost - discount_amount
        return total_cost

if __name__ == '__main__':
    calculator = TieredDiscountCalculator()
    quantities = [0, 10, 55, 105]
    for qty in quantities:
        final_price = calculator.calculate_final_price(qty)
        print(final_price)