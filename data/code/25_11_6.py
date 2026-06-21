class TieredDiscountCalculator:
    PRICE_LIST = {
        1: 10.0,
        2: 15.5,
        3: 20.0,
        4: 25.0,
        5: 30.0
    }

    DISCOUNT_TIERS = [
        (100, 0.10),
        (50, 0.05),
        (0, 0.0)
    ]

    @staticmethod
    def calculate_discount(quantity, item_id):
        unit_price = TieredDiscountCalculator.PRICE_LIST.get(item_id, None)
        if unit_price is None:
            raise ValueError(f"Invalid item_id: {item_id}")
        
        total_price = quantity * unit_price
        
        for threshold, discount_rate in TieredDiscountCalculator.DISCOUNT_TIERS:
            if total_price >= threshold:
                final_price = total_price * (1 - discount_rate)
                return final_price
        
        return total_price

if __name__ == '__main__':
    calculator = TieredDiscountCalculator()
    result1 = TieredDiscountCalculator.calculate_discount(5, 1)
    result2 = TieredDiscountCalculator.calculate_discount(10, 2)
    result3 = TieredDiscountCalculator.calculate_discount(3, 5)
    print(result1)
    print(result2)
    print(result3)