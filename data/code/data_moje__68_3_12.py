import math

CONVERSION_FACTOR = 100
MAX_VALID_AMOUNT = 1000000000.0

class ConversionError(Exception):
    def __init__(self, message: str, original_value):
        super().__init__(message)
        self.original_value = original_value

def validate_numeric_input(value):
    if isinstance(value, bool):
        raise TypeError("Boolean values are not accepted as numeric input.")
    if not isinstance(value, (int, float)):
        raise TypeError(f"Expected numeric type int or float, got {type(value).__name__}")
    if math.isnan(value):
        raise ValueError("Input value cannot be NaN.")
    if math.isinf(value):
        raise ValueError("Input value must be finite.")
    if abs(value) > MAX_VALID_AMOUNT:
        raise OverflowError(f"Input value {value} exceeds maximum allowed limit of {MAX_VALID_AMOUNT}.")

def dollars_to_cents(dollars: float | int) -> int:
    validate_numeric_input(dollars)
    cents_value = dollars * CONVERSION_FACTOR
    rounded_cents = round(cents_value)
    return int(rounded_cents)

if __name__ == '__main__':
    test_cases = [10.50, 0.01, 100, 5.999, -12.34]
    for amount in test_cases:
        try:
            result = dollars_to_cents(amount)
            print(f"${amount} converts to {result} cents")
        except Exception as e:
            print(f"Error converting {amount}: {e}")
    
    try:
        invalid_input = float('nan')
        dollars_to_cents(invalid_input)
    except ValueError as e:
        print(f"Caught expected error for NaN: {e}")
    
    try:
        invalid_bool = True
        dollars_to_cents(invalid_bool)
    except TypeError as e:
        print(f"Caught expected error for boolean: {e}")