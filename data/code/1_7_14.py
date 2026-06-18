import math
from typing import Any

class WeightValidationError(Exception):
    """Base exception for weight validation errors."""
    pass

class InvalidDataTypeError(WeightValidationError):
    """Raised when input is not a numeric type (int or float)."""
    pass

class NegativeWeightError(WeightValidationError):
    """Raised when the input value represents an impossible negative weight."""
    pass

def normalize_weight(value: Any) -> float:
    """
    Validates and normalizes a weight input.

    Args:
        value: The input to validate as int or float, must be positive (or zero).

    Returns:
        The validated numeric weight value as a float.

    Raises:
        InvalidDataTypeError: If the value is not an instance of int or float.
        NegativeWeightError: If the value is negative or NaN/Inf.
    """
    if not isinstance(value, (int, float)):
        raise InvalidDataTypeError(f"Invalid data type for weight '{value}'. Expected a number.")

    normalized_value = float(value)

    # Check for Non-Finite values like NaN or Infinity which are mathematically impossible as physical weights in this context.
    if not math.isfinite(normalized_value):
        raise InvalidDataTypeError(f"Non-finite value {normalized_value} is invalid for weight.")

    if normalized_value < 0:
        raise NegativeWeightError(f"Weight cannot be negative: {value}.")

    return normalized_value

def validate_weight(value: Any) -> float:
    """
    Decorator-like factory that wraps a function to automatically handle input validation.

    This can be used as `@validate_weight` decorator or called manually on functions/methods.
    
    When applied via the '@' syntax, it will wrap any target method/function provided in arguments and return 
    its original callable with an injected first argument for normalization (if the function signature is compatible), 
    otherwise if a string target name is passed it acts as a higher-order decorator factory that wraps specific functions.
    
    Note: Since standard Python decorators work directly on functions, this implementation provides two modes via `apply`.
    If used with '@validate_weight' syntax directly without arguments in the user's mental model of typical usage, 
    usually one would pass an optional inner function or string name if they wanted to use it as a higher-order wrapper factory.
    
    However, strictly adhering to "decorator for a function", we interpret this as creating a utility that acts like:
        @validate_weight(func) -> returns decorated func where the first arg is auto-normalized
    
    But since standard python '@validator' expects `@validator`, let's create an adapter. 
    
    To strictly follow the prompt "Design and implement A decorator", we will provide an implementation of a generic higher-order function that can be used via:
        @validate_weight(lambda f, name="my_func": ...)
        
    Actually, to make it most useful as requested ("automatically validates"), let's create a standard decorator factory 
    where the user passes the function directly or we use introspection on `__name__` if no arguments are passed? No, that breaks signature. 
    
    Let's implement: A higher-order function that wraps ANY target method/function and applies normalization to its first argument automatically.
    
    Usage:
        @validate_weight
        def my_func(weight): ... 
        # Works by capturing 'self' in Python if it detects __func__, otherwise we handle single args specially? No, simpler is best.)
        
    Revised Design for strict "A decorator":
    We will define `decorator_validate` that takes a function object and returns the wrapped version.
    
    Usage: @validate_weight(function) works via apply() or just standard usage where user passes func directly to it if needed? 
    Actually, Python decorators are usually single-line annotations like @validator(func). Let's do that. 
    BUT to make it "automatically" work for a generic function class method context (like 'self'), we will detect if the first arg is 'self'.
    
    If self_detected: normalize inner args else normalizing outer args."""
    
    def decorator(target_func):
        """Decorator factory that wraps target_func with validation logic."""

        name = getattr(target_func, '__name__', 'unknown')
        
        @functools.wraps(target_func)
        def wrapper(*args, **kwargs):
            try:
                # Check if it's a class method (self argument detected as first arg in args list) or standalone function.
                has_self = len(args) > 0 and type(args[0]).__name__ == 'method' if hasattr(type(target_func), '__bases__') else False
                
                normalized_args_list, kwargs_to_use = [], []

                # Simple heuristic: If the first argument is 'self', pass it through without normalization (assuming weight is second arg)
                # OR we assume the FIRST numeric-like arg should be validated. 
                
                # To keep this robust and simple as per task "validates ... input":
                # We will try to validate any positional args that look like weights or just the first one if it's a number? 
                # That might break existing code where 'self' is checked.
                
                pass

            except:
                return target_func(*args, **kwargs)

if __name__ == '__main__':
    pass
