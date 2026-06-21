class DiscountCalculator:
    TIERED_PRICES = {
        'basic': 100,
        'standard': 250,
        'premium': 500,
        'elite': 1000
    }

    DISCOUNT_TIERS = [
        (0, 0),
        (1, 0.95),
        (5, 0.90),
        (10, 0.85),
        (20, 0.80),
        (50, 0.75)
    ]

    @staticmethod
    def calculate_discount(tier_name, quantity):
        if tier_name not in DiscountCalculator.TIERED_PRICES:
            raise ValueError(f"Invalid tier name: {tier_name}")
        if quantity < 0:
            raise ValueError("Quantity must be non-negative")
        
        unit_price = DiscountCalculator.TIERED_PRICES[tier_name]
        total_base_cost = unit_price * quantity
        
        discount_rate = 1.0
        for threshold, rate in DiscountCalculator.DISCOUNT_TIERS:
            if quantity >= threshold:
                discount_rate = rate
            else:
                break
        
        final_cost = total_base_cost * discount_rate
        discount_amount = total_base_cost - final_cost
        
        return {
            'tier': tier_name,
            'quantity': quantity,
            'unit_price': unit_price,
            'base_total': total_base_cost,
            'discount_rate': discount_rate,
            'discount_amount': discount_amount,
            'final_total': final_cost
        }

if __name__ == '__main__':
    sample_tiers = ['basic', 'standard', 'premium', 'elite']
    sample_quantities = [1, 5, 10, 25, 100]
    
    for tier in sample_tiers:
        for qty in sample_quantities:
            result = DiscountCalculator.calculate_discount(tier, qty)
            print(f"Tier: {result['tier']}, Qty: {result['quantity']}, Base: {result['base_total']}, Discount: {result['discount_amount']}, Final: {result['final_total']}")