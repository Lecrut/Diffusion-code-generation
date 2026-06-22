class TieredDiscountCalculator:
    PRICE_LIST = {
        'widget': 100,
        'gadget': 250,
        'doohickey': 500,
        'thingamajig': 1000
    }

    TIER_THRESHOLDS = [
        (5000, 0.20),
        (2000, 0.15),
        (1000, 0.10),
        (500, 0.05),
        (0, 0.0)
    ]

    @staticmethod
    def calculate_discount(total_amount):
        for threshold, rate in TieredDiscountCalculator.TIER_THRESHOLDS:
            if total_amount >= threshold:
                return total_amount * rate
        return 0.0

    @staticmethod
    def get_item_price(item_name):
        return TieredDiscountCalculator.PRICE_LIST.get(item_name.lower(), 0)

    @staticmethod
    def compute_total_with_discount(order_items):
        total = sum(TieredDiscountCalculator.get_item_price(item) for item in order_items)
        discount = TieredDiscountCalculator.calculate_discount(total)
        return total - discount

if __name__ == '__main__':
    calculator = TieredDiscountCalculator()
    sample_order = ['widget', 'gadget', 'doohickey', 'thingamajig', 'widget', 'gadget']
    final_price = calculator.compute_total_with_discount(sample_order)
    print(final_price)