class DiscountCalculator:
    PRICES = {
        'basic': 10.0,
        'standard': 25.0,
        'premium': 50.0,
        'enterprise': 100.0
    }

    @staticmethod
    def calculate_total_cost(items):
        if not items:
            return 0.0
        
        total_raw = 0.0
        for item in items:
            name = item.get('name', '')
            quantity = item.get('quantity', 0)
            price = DiscountCalculator.PRICES.get(name, 0.0)
            total_raw += price * quantity
        
        discount_rate = 0.0
        if total_raw >= 500:
            discount_rate = 0.20
        elif total_raw >= 250:
            discount_rate = 0.15
        elif total_raw >= 100:
            discount_rate = 0.10
        elif total_raw >= 50:
            discount_rate = 0.05
        
        discount_amount = total_raw * discount_rate
        final_total = total_raw - discount_amount
        return round(final_total, 2)

if __name__ == '__main__':
    sample_order = [
        {'name': 'premium', 'quantity': 3},
        {'name': 'standard', 'quantity': 5},
        {'name': 'basic', 'quantity': 10}
    ]
    result = DiscountCalculator.calculate_total_cost(sample_order)
    print(result)