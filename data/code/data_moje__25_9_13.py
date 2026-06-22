class CalculationError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

class NegativeValueError(CalculationError):
    def __init__(self, field_name):
        message = f"{field_name} cannot be negative."
        super().__init__(message)

class InvalidDiscountError(CalculationError):
    def __init__(self):
        message = "Discount percentage cannot exceed 100%."
        super().__init__(message)

DISCOUNT_DIVISOR = 100.0

def validate_price(value):
    if value < 0.0:
        raise NegativeValueError("Original price")

def validate_discount(value):
    if value < 0.0:
        raise NegativeValueError("Discount percentage")
    if value > 100.0:
        raise InvalidDiscountError()

def compute_discounted_price(original_price: float, discount_percentage: float) -> float:
    validate_price(original_price)
    validate_discount(discount_percentage)
    reduction_factor = 1.0 - (discount_percentage / DISCOUNT_DIVISOR)
    return original_price * reduction_factor

if __name__ == '__main__':
    price_one = 150.0
    discount_one = 20.0
    result_one = compute_discounted_price(price_one, discount_one)
    print(result_one)

    price_two = 50.0
    discount_two = 0.0
    result_two = compute_discounted_price(price_two, discount_two)
    print(result_two)

    price_three = 100.0
    discount_three = 100.0
    result_three = compute_discounted_price(price_three, discount_three)
    print(result_three)

    try:
        compute_discounted_price(100.0, 150.0)
    except InvalidDiscountError as e:
        print(e.message)

    try:
        compute_discounted_price(-10.0, 10.0)
    except NegativeValueError as e:
        print(e.message)