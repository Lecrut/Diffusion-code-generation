class DiscountError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InvalidPriceError(DiscountError):
    def __init__(self):
        super().__init__("Original price must be non-negative.")

class InvalidDiscountError(DiscountError):
    def __init__(self, reason):
        super().__init__(f"Discount invalid: {reason}")

def _validate_price(value: float) -> None:
    if value < 0.0:
        raise InvalidPriceError()

def _validate_discount(value: float) -> None:
    if value < 0.0:
        raise InvalidDiscountError("cannot be negative")
    if value > 100.0:
        raise InvalidDiscountError("cannot exceed 100%")

def calculate_final_price(original_price: float, discount_percentage: float) -> float:
    _validate_price(original_price)
    _validate_discount(discount_percentage)
    discount_factor = 1.0 - (discount_percentage / 100.0)
    return original_price * discount_factor

if __name__ == '__main__':
    base_price = 150.0
    sale_discount = 20.0
    final_amount = calculate_final_price(base_price, sale_discount)
    print(final_amount)
    zero_discount = calculate_final_price(150.0, 0.0)
    print(zero_discount)
    full_discount = calculate_final_price(150.0, 100.0)
    print(full_discount)