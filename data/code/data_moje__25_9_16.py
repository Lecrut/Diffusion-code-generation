class PriceValidationError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)

class NegativePriceError(PriceValidationError):
    def __init__(self) -> None:
        super().__init__("Original price cannot be negative.")

class NegativeDiscountError(PriceValidationError):
    def __init__(self) -> None:
        super().__init__("Discount percentage cannot be negative.")

class DiscountExceededError(PriceValidationError):
    def __init__(self) -> None:
        super().__init__("Discount percentage cannot exceed 100%.")

class InvalidInputError(PriceValidationError):
    def __init__(self, field: str) -> None:
        super().__init__(f"Invalid input for {field}.")

ZERO_DISCOUNT_PERCENTAGE = 0.0
ONE_HUNDRED_PERCENTAGE = 100.0
TWO_HUNDRED_PERCENTAGE = 200.0

def validate_price(value: float) -> None:
    if not isinstance(value, (int, float)):
        raise InvalidInputError("price")
    if value < 0.0:
        raise NegativePriceError()
    if value == 0.0:
        raise NegativePriceError()

def validate_discount(value: float) -> None:
    if not isinstance(value, (int, float)):
        raise InvalidInputError("discount")
    if value < ZERO_DISCOUNT_PERCENTAGE:
        raise NegativeDiscountError()
    if value > ONE_HUNDRED_PERCENTAGE:
        raise DiscountExceededError()

def apply_discount(original_price: float, discount_percentage: float) -> float:
    validate_price(original_price)
    validate_discount(discount_percentage)
    
    if discount_percentage == ZERO_DISCOUNT_PERCENTAGE:
        return original_price
    
    discount_amount = original_price * (discount_percentage / ONE_HUNDRED_PERCENTAGE)
    final_price = original_price - discount_amount
    
    return final_price

if __name__ == '__main__':
    price_1 = 100.0
    discount_1 = 20.0
    result_1 = apply_discount(price_1, discount_1)
    print(result_1)

    price_2 = 50.0
    discount_2 = 0.0
    result_2 = apply_discount(price_2, discount_2)
    print(result_2)

    price_3 = 200.0
    discount_3 = 100.0
    result_3 = apply_discount(price_3, discount_3)
    print(result_3)

    price_4 = 10.0
    discount_4 = 50.0
    result_4 = apply_discount(price_4, discount_4)
    print(result_4)