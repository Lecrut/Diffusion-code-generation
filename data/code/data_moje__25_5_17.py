class DiscountCalculator:
    def __init__(self, original_price, discount_percentage):
        if not isinstance(original_price, (int, float)) or original_price < 0:
            raise ValueError("Original price must be a non-negative number")
        if not isinstance(discount_percentage, (int, float)) or discount_percentage < 0 or discount_percentage > 100:
            raise ValueError("Discount percentage must be between 0 and 100")
        self.original_price = original_price
        self.discount_percentage = discount_percentage

    def calculate(self):
        discount_amount = self.original_price * (self.discount_percentage / 100)
        final_price = self.original_price - discount_amount
        return self.original_price, discount_amount, final_price

if __name__ == '__main__':
    calculator = DiscountCalculator(99.99, 30)
    result = calculator.calculate()
    print(result)