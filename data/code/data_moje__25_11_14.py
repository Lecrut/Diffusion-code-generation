class DiscountCalculator:
    PRICES = {
        'item_a': 10,
        'item_b': 20,
        'item_c': 30
    }

    DISCOUNT_TIERS = [
        (100, 0.20),
        (50, 0.10),
        (0, 0)
    ]

    @staticmethod
    def calculate_total_discount(items, quantities):
        total_cost = 0
        for item in items:
            if item not in DiscountCalculator.PRICES:
                raise ValueError(f"Unknown item: {item}")
            total_cost += DiscountCalculator.PRICES[item] * quantities[item]

        discount_rate = 0
        for threshold, rate in DiscountCalculator.DISCOUNT_TIERS:
            if total_cost >= threshold:
                discount_rate = rate
                break

        return total_cost * discount_rate

    @staticmethod
    def get_discounted_total(items, quantities):
        total_cost = 0
        for item in items:
            if item not in DiscountCalculator.PRICES:
                raise ValueError(f"Unknown item: {item}")
            total_cost += DiscountCalculator.PRICES[item] * quantities[item]

        discount_rate = 0
        for threshold, rate in DiscountCalculator.DISCOUNT_TIERS:
            if total_cost >= threshold:
                discount_rate = rate
                break

        return total_cost - (total_cost * discount_rate)

if __name__ == '__main__':
    sample_items = ['item_a', 'item_b', 'item_c']
    sample_quantities = {
        'item_a': 5,
        'item_b': 3,
        'item_c': 2
    }
    result = DiscountCalculator.get_discounted_total(sample_items, sample_quantities)
    print(result)