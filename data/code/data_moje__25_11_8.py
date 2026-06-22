class TieredDiscountCalculator:
    PRICE_LIST = {
        "widget": 25.00,
        "gadget": 50.00,
        "doohickey": 75.00,
        "thingamajig": 100.00
    }
    
    TIER_THRESHOLDS = [
        (1000, 0.20),
        (500, 0.15),
        (200, 0.10),
        (0, 0.05)
    ]

    @staticmethod
    def calculate_total_discount(items):
        subtotal = 0.0
        for item, quantity in items.items():
            if item in TieredDiscountCalculator.PRICE_LIST:
                price = TieredDiscountCalculator.PRICE_LIST[item]
                subtotal += price * quantity
        
        discount_rate = 0.0
        for threshold, rate in TieredDiscountCalculator.TIER_THRESHOLDS:
            if subtotal >= threshold:
                discount_rate = rate
                break
        
        discount_amount = subtotal * discount_rate
        final_total = subtotal - discount_amount
        return {
            "subtotal": subtotal,
            "discount_rate": discount_rate,
            "discount_amount": discount_amount,
            "final_total": final_total
        }

if __name__ == '__main__':
    calculator = TieredDiscountCalculator()
    
    test_order_1 = {"widget": 5, "gadget": 2}
    result_1 = calculator.calculate_total_discount(test_order_1)
    print(result_1)
    
    test_order_2 = {"doohickey": 10, "thingamajig": 5}
    result_2 = calculator.calculate_total_discount(test_order_2)
    print(result_2)
    
    test_order_3 = {"widget": 100}
    result_3 = calculator.calculate_total_discount(test_order_3)
    print(result_3)