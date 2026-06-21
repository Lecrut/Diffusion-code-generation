class DiscountCalculator:
    FIXED_PRICES = {
        "basic": 10,
        "standard": 25,
        "premium": 50,
        "enterprise": 100
    }

    TIERS = [
        (100, 0),
        (500, 0.05),
        (1000, 0.10),
        (5000, 0.15),
        (10000, 0.20)
    ]

    @staticmethod
    def calculate_tiered_discount(product_type: str, quantity: int) -> float:
        if product_type not in DiscountCalculator.FIXED_PRICES:
            raise ValueError(f"Invalid product type: {product_type}")
        
        base_price = DiscountCalculator.FIXED_PRICES[product_type]
        total_value = base_price * quantity
        
        discount_rate = 0.0
        for threshold, rate in DiscountCalculator.TIERS:
            if total_value >= threshold:
                discount_rate = rate
        
        return round(total_value * (1 - discount_rate), 2)

if __name__ == '__main__':
    sample_product = "premium"
    sample_quantity = 25
    
    result = DiscountCalculator.calculate_tiered_discount(sample_product, sample_quantity)
    print(f"Total cost for {sample_quantity} {sample_product} items: ${result}")
    
    sample_product_2 = "standard"
    sample_quantity_2 = 50
    
    result_2 = DiscountCalculator.calculate_tiered_discount(sample_product_2, sample_quantity_2)
    print(f"Total cost for {sample_quantity_2} {sample_product_2} items: ${result_2}")
    
    sample_product_3 = "enterprise"
    sample_quantity_3 = 10
    
    result_3 = DiscountCalculator.calculate_tiered_discount(sample_product_3, sample_quantity_3)
    print(f"Total cost for {sample_quantity_3} {sample_product_3} items: ${result_3}")