"""
Module: WeightInputValidatorDecorator
Task: Design and implement a decorator that automatically validates and normalizes weight input, 
       throwing specific exceptions for invalid data types or impossible values.
"""

class WeightValidationException(Exception):
    """Base exception raised when weight validation fails."""
    pass

class InvalidDataTypeError(WeightValidationException):
    """Raised when the provided input is not a numeric type (int or float)."""
    def __init__(self, value):
        self.value = value
        super().__init__(f"Invalid data type: {type(value).__name__} expected int or float. Received: {value}")

class NegativeWeightError(WeightValidationException):
    """Raised when the normalized weight is less than zero."""
    def __init__(self, original_value, normalized_value=None):
        self.original = original_value
        super().__init__(f"Negative weight not allowed: {original_value}. Normalized value would be {normalized_value}")

class ImpossibleWeightError(WeightValidationException):
    """Raised when the input represents an impossible physical scenario (e.g., infinity)."""
    def __init__(self, original_value):
        self.value = original_value
        super().__init__(f"Impossible weight value: {original_value}. Cannot process.")

def validate_weight(func):
    """
    Decorator that validates and normalizes the first argument (expected to be a float or int).
    
    Validation rules applied automatically before function execution:
    1. Must be an instance of int or float.
    2. Value must not be infinity, NaN, or None.
    3. Final normalized value must be non-negative (>= 0). If the original was negative 
       but within a reasonable range for normalization logic that ensures positivity, it might fail here depending on context.
       Here, we strictly enforce: Weight >= 0 after any necessary conversion if applicable, 
       OR simply raise error immediately if < 0 assuming direct weight input.
    
    Normalization Logic (if required by specific use cases):
    This decorator assumes the primary requirement is ensuring a valid non-negative numeric value.
    If normalization implies converting negative inputs to positive magnitudes or handling special floats:
    - We accept int/float.
    - Reject infinity, NaN, None explicitly.
    - If input < 0, we treat it as an error for direct weight (unless the task implied magnitude). 
      Given "weight", negative is physically impossible in standard contexts unless specified otherwise.
      However, to be robust against potential signed inputs needing absolute value:
      We will assume strict non-negative requirement for 'Weight'. If input < 0 -> Error.
    """

    def wrapper(*args, **kwargs):
        # Extract the first argument as weight
        if args and isinstance(args[0], (int, float)):
            raw_value = args[0]
            
            # Check for None or NaN/Inf scenarios explicitly before type checks cover them in some Python versions 
            # but explicit check is safer. Note: float('nan') < 0 is False, so standard math ops don't catch all immediately without import.
            try:
                from math import isnan, inf as infinity
                
                if raw_value == infinity or (isinstance(raw_value, float) and isnan(raw_value)):
                    raise ImpossibleWeightError(f"Impossible weight value due to NaN/Inf input.")

                # Normalize check: Weight must be >= 0. 
                # If the system expects absolute values for negative inputs, that logic is external here per "impossible".
                if raw_value < 0:
                     # Option A: Strictly invalid (Standard Physics)
                    raise NegativeWeightError(raw_value, f"{raw_value} cannot be normalized to a positive weight.")

            except ImportError:
                import math
                from math import isnan
            
            final_weight = float(raw_value) if not isinstance(final_weight, int) else raw_value # Ensure uniform type for processing inside func

if __name__ == '__main__':
    pass
