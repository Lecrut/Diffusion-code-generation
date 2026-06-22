class DiscountCalculator:
    FIXED_PRICES = {
        "standard": 100.0,
        "premium": 250.0,
        "ultimate": 500.0
    }

    DISCOUNT_TIERS = [
        (1, 0.0),
        (10, 0.05),
        (50, 0.10),
        (100, 0.15)
    ]

    @staticmethod
    def calculate_tiered_discount(product_type: str, quantity: int) -> float:
        if product_type not in DiscountCalculator.FIXED_PRICES:
            raise ValueError(f"Invalid product type: {product_type}")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        
        base_price = DiscountCalculator.FIXED_PRICES[product_type]
        total_before_discount = base_price * quantity
        
        discount_rate = 0.0
        for tier_quantity, tier_rate in DiscountCalculator.DISCOUNT_TIERS:
            if quantity >= tier_quantity:
                discount_rate = tier_rate
        
        discount_amount = total_before_discount * discount_rate
        return discount_amount

if __name__ == '__main__':
    test_cases = [
        ("standard", 5),
        ("premium", 12),
        ("ultimate", 55),
        ("standard", 150)
    ]
    
    for prod_type, qty in test_cases:
        result = DiscountCalculator.calculate_tiered_discount(prod_type, qty)
        print(f"Product: {prod_type}, Quantity: {qty}, Discount Amount: {result:.2f}")