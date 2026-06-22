class PriceCalculationError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class NegativePriceError(PriceCalculationError):
    def __init__(self):
        super().__init__("The original price cannot be negative.")

class NegativeDiscountError(PriceCalculationError):
    def __init__(self):
        super().__init__("The discount percentage cannot be negative.")

class ExcessiveDiscountError(PriceCalculationError):
    def __init__(self):
        super().__init__("The discount percentage cannot exceed 100.")

def _validate_price(value: float) -> None:
    if value < 0.0:
        raise NegativePriceError()

def _validate_discount(value: float) -> None:
    if value < 0.0:
        raise NegativeDiscountError()
    if value > 100.0:
        raise ExcessiveDiscountError()

def calculate_final_price(original_price: float, discount_percentage: float) -> float:
    _validate_price(original_price)
    _validate_discount(discount_percentage)
    multiplier = 1.0 - (discount_percentage / 100.0)
    final_amount = original_price * multiplier
    return final_amount

def format_currency(value: float) -> str:
    formatted = f"${value:.2f}"
    return formatted

if __name__ == '__main__':
    standard_price = 150.0
    standard_discount = 25.0
    result_standard = calculate_final_price(standard_price, standard_discount)
    print(format_currency(result_standard))
    
    zero_discount_price = 50.0
    zero_discount = 0.0
    result_zero = calculate_final_price(zero_discount_price, zero_discount)
    print(format_currency(result_zero))
    
    full_discount_price = 300.0
    full_discount = 100.0
    result_full = calculate_final_price(full_discount_price, full_discount)
    print(format_currency(result_full))
    
    try:
        calculate_final_price(-10.0, 10.0)
    except PriceCalculationError as e:
        print(e.message)
    
    try:
        calculate_final_price(100.0, 110.0)
    except PriceCalculationError as e:
        print(e.message)