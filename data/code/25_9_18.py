MAX_DISCOUNT = 100.0
MIN_VALUE = 0.0

class InvalidPriceException(Exception):
    def __init__(self, message):
        super().__init__(message)

class InvalidDiscountException(Exception):
    def __init__(self, message):
        super().__init__(message)

def validate_inputs(base: float, pct: float) -> None:
    if base < MIN_VALUE:
        raise InvalidPriceException("Base price must be non-negative")
    if pct < MIN_VALUE:
        raise InvalidDiscountException("Discount percentage must be non-negative")
    if pct > MAX_DISCOUNT:
        raise InvalidDiscountException("Discount percentage cannot exceed 100%")

def apply_discount(base: float, pct: float) -> float:
    validate_inputs(base, pct)
    multiplier = 1.0 - (pct / MAX_DISCOUNT)
    return base * multiplier

if __name__ == '__main__':
    original = 100.0
    discount = 20.0
    final = apply_discount(original, discount)
    print(final)
    
    test_zero = apply_discount(50.0, 0.0)
    print(test_zero)
    
    test_full = apply_discount(200.0, 100.0)
    print(test_full)
    
    test_half = apply_discount(75.5, 50.0)
    print(test_half)