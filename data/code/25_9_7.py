class PriceCalculationError(Exception):
    def __init__(self, message):
        super().__init__(message)

class NegativePriceError(PriceCalculationError):
    def __init__(self):
        super().__init__("Original price cannot be negative.")

class NegativeDiscountError(PriceCalculationError):
    def __init__(self):
        super().__init__("Discount percentage cannot be negative.")

class ExcessiveDiscountError(PriceCalculationError):
    def __init__(self):
        super().__init__("Discount percentage cannot exceed 100%.")

def _ensure_valid_price(value: float) -> None:
    if value < 0:
        raise NegativePriceError()

def _ensure_valid_discount(value: float) -> None:
    if value < 0:
        raise NegativeDiscountError()
    if value > 100:
        raise ExcessiveDiscountError()

def calculate_final_price(original_price: float, discount_percentage: float) -> float:
    _ensure_valid_price(original_price)
    _ensure_valid_discount(discount_percentage)
    discount_value = original_price * (discount_percentage / 100.0)
    return original_price - discount_value

def run_tests() -> None:
    test_cases = [
        (100.0, 20.0),
        (50.0, 0.0),
        (200.0, 100.0),
        (15.50, 10.0)
    ]
    for price, discount in test_cases:
        final = calculate_final_price(price, discount)
        print(final)

if __name__ == '__main__':
    run_tests()