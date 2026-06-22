class PricingException(Exception):
    def __init__(self, message):
        super().__init__(message)

class NegativeValueError(PricingException):
    def __init__(self, field_name):
        super().__init__(f"{field_name} cannot be negative.")

class InvalidDiscountError(PricingException):
    def __init__(self):
        super().__init__("Discount percentage cannot exceed 100%.")

def validate_price(value):
    if value < 0:
        raise NegativeValueError("Original price")
    return True

def validate_discount(value):
    if value < 0:
        raise NegativeValueError("Discount percentage")
    if value > 100:
        raise InvalidDiscountError()
    return True

def apply_discount_logic(price, discount):
    multiplier = 1.0 - (discount / 100.0)
    return price * multiplier

def calculate_final_price(original_price: float, discount_percent: float) -> float:
    validate_price(original_price)
    validate_discount(discount_percent)
    return apply_discount_logic(original_price, discount_percent)

if __name__ == '__main__':
    base_price = 150.0
    disc_rate = 25.0
    final_result = calculate_final_price(base_price, disc_rate)
    print(final_result)
    
    full_disc_result = calculate_final_price(50.0, 100.0)
    print(full_disc_result)
    
    no_disc_result = calculate_final_price(50.0, 0.0)
    print(no_disc_result)