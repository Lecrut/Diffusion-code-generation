class DiscountCalculator:
    def __init__(self, original_price, discount_percentage):
        self.original_price = original_price
        self.discount_percentage = discount_percentage

    def compute_discount_value(self):
        return self.original_price * (self.discount_percentage / 100.0)

    def compute_final_price(self):
        discount_value = self.compute_discount_value()
        return self.original_price - discount_value

    def get_results(self):
        return {
            "original_price": self.original_price,
            "discount_percentage": self.discount_percentage,
            "calculated_discount_value": self.compute_discount_value(),
            "final_price": self.compute_final_price()
        }

if __name__ == '__main__':
    product_price = 500.0
    reduction_rate = 25.0
    
    calc = DiscountCalculator(product_price, reduction_rate)
    
    details = calc.get_results()
    print(details)
    
    final_cost = calc.compute_final_price()
    print(final_cost)