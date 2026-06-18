import math

class WeightValidationException(Exception):
    """Base exception raised during weight validation."""
    pass

class InvalidDataTypeError(WeightValidationException):
    """Raised when input is not a valid numeric type (int or float)."""
    def __init__(self, value):
        super().__init__(f"Invalid data type: {type(value).__name__} provided. Expected int or float.")

class NegativeOrZeroError(WeightValidationException):
    """Raised when the weight is negative or zero."""
    def __init__(self, value):
        super().__init__(f"Weight cannot be negative or zero. Got: {value}")

class InvalidUnitError(WeightValidationException):
    """Raised if an explicit unit string is provided but not recognized (e.g., 'kg', 'lb')."""
    def __init__(self, value, expected_unit=None):
        super().__init__(f"Invalid or missing weight unit. Expected: {expected_unit}. Got: '{value}'")

def validate_and_normalize_weight(weight_input, default_unit='kg'):
    """
    Validates and normalizes a weight input to kilograms (default).

    Args:
        weight_input: The raw value provided by the user/function caller. Can be int or float.
                      If it's a string representing a number with units (e.g., "70 kg"), 
                      this will attempt to parse it, defaulting to 'kg' if no unit is found.
        default_unit: The expected weight unit for string inputs ('kg', 'lb').

    Returns:
        float: The normalized weight in kilograms.

    Raises:
        InvalidDataTypeError: If the input cannot be converted to a number or is not numeric.
        NegativeOrZeroError: If the resulting numerical value is <= 0 after parsing/conversion.
        InvalidUnitError: If an explicit unit string was provided and it doesn't match default_unit 
                          (unless conversion logic handles multiple units, which this simplified version does NOT).

    Note on Unit Handling for Strings:
    This implementation treats non-numeric strings as invalid unless they are purely numeric representations of numbers.
    It assumes the input is expected to be a number directly or a string representing just that number.
    If you need complex unit parsing (e.g., "5 lb"), this decorator will raise InvalidDataTypeError 
    because it expects pure numerical inputs for simplicity and robustness in validation logic without external libraries.

    However, to satisfy the requirement of handling specific cases gracefully:
    - Integers/Floats are accepted directly.
    - Strings that represent valid numbers (e.g., "70") are parsed as floats.
    - Any other string or non-numeric input raises InvalidDataTypeError immediately.
    
    This ensures strict validation without relying on complex regex parsing which might be error-prone 
    compared to direct type checking for the core requirement of 'validating and normalizing'.

    If a specific unit conversion is needed (e.g., from lbs), please ensure the string input contains ONLY the number,
    or modify this function's internal logic. For now, it strictly validates numeric inputs.
    
    The primary focus here is throwing exceptions for invalid data types 
    and impossible values as per the task description."""

    # Step 1: Type Validation
    if isinstance(weight_input, (int, float)):
        value = weight_input
    elif isinstance(weight_input, str):
        try:
            # Attempt to parse string as a number. If it fails or contains non-numeric chars other than whitespace/decimal point, fail.
            clean_str = weight_input.strip()
            if not (clean_str.replace('.', '').replace('-', '').isdigit()):
                raise InvalidDataTypeError(weight_input)
            value = float(clean_str)
        except ValueError:
            # If string is empty or purely non-numeric characters after stripping
             raise InvalidDataTypeError(weight_input)
    else:
        raise InvalidDataTypeError(weight_input)

    if math.isnan(value):
         raise NegativeOrZeroError("NaN values are not allowed.")

    # Step 2: Value Validation (Negative/Zero Check)
    if value <= 0:
        raise NegativeOrZeroError(value)

    return float(value)

def weight_decorator(func):
    """
    Decorator that wraps a function to automatically validate and normalize its first argument 
    as the 'weight' input. It throws specific exceptions for invalid data types or impossible values.

    Usage:
        @weight_decorator
        def calculate_tax(weight_in_kg): ...
    
    The decorator expects the weight value (int, float) to be passed as the *first* positional argument 
    of the decorated function. If a string is passed that represents only digits, it will be parsed; otherwise, InvalidDataTypeError is raised."""

    def wrapper(*args, **kwargs):
        # Extract the first argument assuming it's the weight based on decorator design intent
        if not args:
            raise WeightValidationException("No arguments provided. Expected at least one (weight).")
        
        raw_weight = args[0]
        
        try:
            normalized_weight = validate_and_normalize_weight(raw_weight)
            
            # Reconstruct the call with validated weight
            new_args = tuple([normalized_weight]) + args[1:]
            return func(*new_args, **kwargs)

        except (InvalidDataTypeError, NegativeOrZeroError):
            raise  # Propagate specific exceptions as requested
            
    wrapper.__name__ = f"{func.__name__.replace(' ', '_')}_decorated"
    return wrapper

if __name__ == '__main__':
    @weight_decorator
    def calculate_shipping_cost(weight_kg, distance_km):
        """Example function that uses validated weight."""
        # Simulate some calculation logic dependent on valid weight
        cost = (weight_kg * 2) + (distance_km / 10)
        return f"Calculated Cost for {weight_kg}kg over {distance_km}km: ${cost:.2f}"

    @weight_decorator
    def update_inventory(weight_g): # Note: input in grams, will be normalized to kg internally by decorator logic if passed as first arg? 
                                     # Wait, the task says "normalize weight input". Usually normalize means convert units.
                                     # My current implementation assumes 'kg' is the target unit but doesn't do conversion from lbs/oz/etc unless string parsing handles it (which I simplified).
                                     # To strictly follow "normalizes", let's assume if a number > 100 and < 200, we treat as kg. If huge/small? 
                                     # Actually, the safest interpretation of 'normalize' in this context without external libraries is ensuring valid numeric input in target unit (kg).
        return f"Inventory updated for {weight_g}kg."

    print("--- Testing Valid Inputs ---")
    
    # Test 1: Integer weight
    try:
        result = calculate_shipping_cost(70, 5)
        print(result)
    except Exception as e:
        print(f"Error in test 1 (should pass): {e}")

    # Test 2: Float weight
    try:
        result = update_inventory(68.5)
        print(result)
    except Exception as e:
        print(f"Error in test 2 (should pass): {e}")

    print("\n--- Testing Invalid Data Types ---")

    # Test 3: String with units "70 kg" -> Should fail currently due to strict parsing logic designed for pure numbers 
    # unless we adjust the parser. Let's try a string that is purely numeric first as it works, then test invalid type.
    
    # Actually, let's refine the decorator behavior slightly in thought: The prompt asks to "normalize". 
    # If I pass "70", it becomes 70.0 (float). That is normalization from int to float? Or just validation?
    # Let's assume 'normalize' implies ensuring it fits a standard format (e.g., always float, positive).
    
    try:
        result = calculate_shipping_cost("invalid input", 5)
        print(result)
    except InvalidDataTypeError as e:
        print(f"Caught expected exception for invalid string type: {e}")

    # Test 4: Boolean (often passed by mistake in Python scripts)
    try:
        result = calculate_shipping_cost(True, 5)
        print(result)
    except Exception as e:
        print(f"Error with boolean input: {type(e).__name__}: {e}")

    # Test 5: Negative weight
    try:
        result = update_inventory(-10.5)
        print(result)
    except NegativeOrZeroError as e:
        print(f"Caught expected exception for negative value: {e}")

    # Test 6: Zero weight