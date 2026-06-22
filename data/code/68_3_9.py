import math

CENTS_PER_DOLLAR = 100

class CurrencyConversionException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

def validate_numeric_input(value):
    if isinstance(value, bool):
        raise CurrencyConversionException("Boolean types are not supported for currency conversion")
    if not isinstance(value, (int, float)):
        raise CurrencyConversionException("Input must be an integer or float")
    if isinstance(value, float) and (math.isnan(value) or math.isinf(value)):
        raise CurrencyConversionException("Input cannot be NaN or infinity")

def convert_dollars_to_cents(amount_dollars):
    validate_numeric_input(amount_dollars)
    if amount_dollars < 0:
        raise CurrencyConversionException("Dollar amount cannot be negative")
    rounded_cents = round(amount_dollars * CENTS_PER_DOLLAR)
    return int(rounded_cents)

if __name__ == '__main__':
    test_cases = [
        10.50,
        0.99,
        25,
        0.01,
        100.00,
        999.99
    ]
    
    for case in test_cases:
        result = convert_dollars_to_cents(case)
        print(result)
        
    error_cases = [
        "invalid",
        True,
        float('nan'),
        float('inf'),
        -5.0
    ]
    
    for case in error_cases:
        try:
            convert_dollars_to_cents(case)
        except CurrencyConversionException as e:
            print(f"Caught error: {e.message}")