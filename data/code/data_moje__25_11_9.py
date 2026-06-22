class TieredDiscountCalculator:
    PRICE_LIST = {
        'item_a': 100.0,
        'item_b': 200.0,
        'item_c': 300.0,
        'item_d': 400.0,
        'item_e': 500.0
    }

    DISCOUNT_TIERS = [
        (1000.0, 0.20),
        (500.0, 0.10),
        (0.0, 0.0)
    ]

    @staticmethod
    def calculate_discount(total_amount):
        for threshold, discount_rate in TieredDiscountCalculator.DISCOUNT_TIERS:
            if total_amount >= threshold:
                return total_amount * discount_rate
        return 0.0

    @classmethod
    def get_item_total(cls, items):
        total = 0.0
        for item_id, quantity in items:
            if item_id in cls.PRICE_LIST:
                total += cls.PRICE_LIST[item_id] * quantity
        return total

    @classmethod
    def get_final_price(cls, items):
        subtotal = cls.get_item_total(items)
        discount = cls.calculate_discount(subtotal)
        return subtotal - discount

if __name__ == '__main__':
    sample_items = [
        ('item_a', 5),
        ('item_b', 3),
        ('item_c', 2)
    ]
    calculator = TieredDiscountCalculator()
    subtotal = TieredDiscountCalculator.get_item_total(sample_items)
    discount = TieredDiscountCalculator.calculate_discount(subtotal)
    final_price = TieredDiscountCalculator.get_final_price(sample_items)
    print(subtotal)
    print(discount)
    print(final_price)