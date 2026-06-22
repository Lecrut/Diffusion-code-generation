class DiscountCalculator:
    def __init__(self):
        self.price_list = {
            'A': 100.0,
            'B': 200.0,
            'C': 300.0,
            'D': 400.0,
        }
        self.discount_tiers = [
            (10, 0.05),
            (20, 0.10),
            (50, 0.15),
            (100, 0.20),
        ]

    @staticmethod
    def calculate_discount(price, quantity):
        base_cost = price * quantity
        
        tier_threshold = 0
        discount_rate = 0.0
        
        for threshold, rate in [(10, 0.05), (20, 0.10), (50, 0.15), (100, 0.20)]:
            if quantity >= threshold:
                tier_threshold = threshold
                discount_rate = rate
            else:
                break
        
        discount_amount = base_cost * discount_rate
        final_price = base_cost - discount_amount
        
        return final_price

if __name__ == '__main__':
    calculator = DiscountCalculator()
    
    price = 100.0
    quantity = 25
    
    final_price = calculator.calculate_discount(price, quantity)
    
    print(final_price)
    
    price_b = 200.0
    quantity_b = 50
    
    final_price_b = calculator.calculate_discount(price_b, quantity_b)
    
    print(final_price_b)