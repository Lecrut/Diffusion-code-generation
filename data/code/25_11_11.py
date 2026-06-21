class DiscountCalculator:
    @staticmethod
    def calculate_total_price(base_price, quantity):
        if quantity == 0:
            return 0.0
        
        if quantity < 10:
            rate = 1.0
        elif quantity < 50:
            rate = 0.95
        elif quantity < 100:
            rate = 0.90
        elif quantity < 200:
            rate = 0.85
        else:
            rate = 0.80
        
        total_before_discount = base_price * quantity
        discount_amount = total_before_discount * (1 - rate)
        final_price = total_before_discount - discount_amount
        return final_price

if __name__ == '__main__':
    price_per_unit = 10.0
    quantities = [5, 25, 75, 150, 250]
    results = []
    for qty in quantities:
        result = DiscountCalculator.calculate_total_price(price_per_unit, qty)
        results.append((qty, result))
    
    for qty, total in results:
        print(f"Quantity: {qty}, Total: {total:.2f}")