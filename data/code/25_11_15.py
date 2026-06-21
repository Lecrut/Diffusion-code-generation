class DiscountCalculator:
    @staticmethod
    def calculate_tiered_discount(base_price, quantity):
        if not isinstance(base_price, (int, float)) or base_price < 0:
            raise ValueError("Base price must be a non-negative number")
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a non-negative integer")
        
        rate = 0.0
        if quantity >= 100:
            rate = 0.20
        elif quantity >= 50:
            rate = 0.15
        elif quantity >= 20:
            rate = 0.10
        elif quantity >= 10:
            rate = 0.05
        
        total_cost = base_price * quantity
        discount_amount = total_cost * rate
        final_price = total_cost - discount_amount
        return final_price, rate, discount_amount

if __name__ == '__main__':
    sample_price = 25.00
    sample_quantity = 75
    final_price, applied_rate, discount_val = DiscountCalculator.calculate_tiered_discount(sample_price, sample_quantity)
    print(final_price)
    print(applied_rate)
    print(discount_val)