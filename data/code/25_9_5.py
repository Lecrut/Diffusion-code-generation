class PriceValidationError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

class NegativePriceError(PriceValidationError):
    def __init__(self):
        super().__init__("Original price must be non-negative.")

class NegativeDiscountError(PriceValidationError):
    def __init__(self):
        super().__init__("Discount percentage cannot be negative.")

class ExcessiveDiscountError(PriceValidationError):
    def __init__(self):
        super().__init__("Discount percentage cannot exceed 100%.")

def _validate_price(value: float) -> None:
    if value < 0.0:
        raise NegativePriceError()

def _validate_discount(value: float) -> None:
    if value < 0.0:
        raise NegativeDiscountError()
    if value > 100.0:
        raise ExcessiveDiscountError()

def apply_discount(value: float, rate: float) -> float:
    return value * (1.0 - rate / 100.0)

def calculate_final_price(original_price: float, discount_percentage: float) -> float:
    _validate_price(original_price)
    _validate_discount(discount_percentage)
    return apply_discount(original_price, discount_percentage)

class PriceCalculator:
    def __init__(self, base_price: float, discount_rate: float):
        self.base_price = base_price
        self.discount_rate = discount_rate

    def get_final_price(self) -> float:
        return calculate_final_price(self.base_price, self.discount_rate)

if __name__ == '__main__':
    standard_price = 150.0
    standard_discount = 20.0
    print(calculate_final_price(standard_price, standard_discount))
    zero_discount = 0.0
    print(calculate_final_price(standard_price, zero_discount))
    full_discount = 100.0
    print(calculate_final_price(standard_price, full_discount))
    calculator = PriceCalculator(200.0, 25.0)
    print(calculator.get_final_price())