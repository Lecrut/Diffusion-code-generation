class DiscountCalculator:
    PRICE_LIST = {
        "item_A": 100,
        "item_B": 200,
        "item_C": 300
    }

    TIER_THRESHOLDS = [
        (1000, 0.0),
        (2500, 0.05),
        (5000, 0.10),
        (10000, 0.15),
        (float('inf'), 0.20)
    ]

    @staticmethod
    def calculate_total_cost(items):
        if not items:
            return 0.0
        
        total_base_price = 0.0
        for item in items:
            if item in DiscountCalculator.PRICE_LIST:
                total_base_price += DiscountCalculator.PRICE_LIST[item]
            else:
                raise ValueError(f"Unknown item: {item}")

        if total_base_price <= 0:
            return 0.0

        discount_rate = 0.0
        for threshold, rate in DiscountCalculator.TIER_THRESHOLDS:
            if total_base_price < threshold:
                discount_rate = rate
                break

        discount_amount = total_base_price * discount_rate
        final_cost = total_base_price - discount_amount
        return final_cost

if __name__ == '__main__':
    items = ["item_A", "item_A", "item_B", "item_B", "item_C"]
    result = DiscountCalculator.calculate_total_cost(items)
    print(result)