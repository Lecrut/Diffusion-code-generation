class TieredDiscountCalculator:
    PRICE_LIST = {
        "A": 100,
        "B": 200,
        "C": 300,
    }
    TIER_RULES = [
        (10, 0.10),
        (5, 0.05),
        (0, 0.00),
    ]

    @staticmethod
    def calculate_total(items):
        total_price = 0
        for item_name, quantity in items:
            base_price = TieredDiscountCalculator.PRICE_LIST[item_name]
            total_price += base_price * quantity
        
        total_discount = 0
        for threshold, rate in TieredDiscountCalculator.TIER_RULES:
            if total_price > threshold:
                total_discount += total_price * rate
                break
        
        final_price = total_price - total_discount
        return final_price

if __name__ == '__main__':
    calculator = TieredDiscountCalculator()
    items = [("A", 10), ("B", 2)]
    result = TieredDiscountCalculator.calculate_total(items)
    print(result)