import math

class WeightValidationError(Exception):
    """Base exception for weight validation errors."""
    pass

class InvalidDataTypeError(WeightValidationError):
    """Raised when input is not a valid number type (int or float)."""
    pass

class NegativeOrZeroError(WeightValidationError):
    """Raised when the normalized value is negative, zero, or infinity."""
    pass

def validate_and_normalize_weight(func):
    def wrapper(*args, **kwargs):
        # Extract weight argument; assume it's either positional first arg 
        # or explicitly passed. For this decorator pattern, we'll expect a 'weight' kwarg.
        if not hasattr(functional_wrapper := func.__wrapped__, '__name__'):
            return func

if __name__ == '__main__':
    pass
