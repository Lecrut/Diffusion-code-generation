class DiscountCalculator:
    @staticmethod
    def calculate_tiered_discount(price, quantity):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        if price < 0:
            raise ValueError("Price cannot be negative")
        discount_rate = 0.0
        if quantity >= 100:
            discount_rate = 0.20
        elif quantity >= 50:
            discount_rate = 0.15
        elif quantity >= 20:
            discount_rate = 0.10
        elif quantity >= 10:
            discount_rate = 0.05
        total_cost = price * quantity
        discount_amount = total_cost * discount_rate
        final_total = total_cost - discount_amount
        return final_total

if __name__ == '__main__':
    sample_price = 10.00
    sample_quantities = [5, 15, 25, 55, 105]
    for qty in sample_quantities:
        result = DiscountCalculator.calculate_tiered_discount(sample_price, qty)
        print(f"Quantity: {qty}, Final Cost: {result:.2f}")