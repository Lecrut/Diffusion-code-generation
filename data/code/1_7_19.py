"""
Module to validate and normalize weight inputs using a decorator pattern.
Throws specific exceptions for invalid data types, non-positive values, 
or physically impossible weights (e.g., exceeding 1000 kg).
"""

class WeightValidationException(Exception):
    """Base exception for weight validation errors."""
    pass

class InvalidDataTypeError(WeightValidationException):
    """Raised when the input is not a valid numeric type."""
    def __init__(self, value):
        super().__init__(f"Invalid data type: {type(value).__name__}. Expected int or float.")

class NonPositiveValueError(WeightValidationException):
    """Raised when the weight is zero or negative."""
    def __init__(self, value):
        super().__init__(f"Non-positive weight detected: {value}")

class ImpossibleWeightError(WeightValidationException):
    """Raised when the weight exceeds a physically reasonable limit (1000 kg)."""
    def __init__(self, value):
        super().__init__(f"Impossible weight detected: {value} kg. Maximum allowed is 1000 kg.")

def validate_weight(func):
    """
    Decorator that validates and normalizes the first argument of a function as a weight.

    Args:
        func (callable): The target function to decorate.

    Returns:
        callable: A wrapper function with validation logic.
    
    Raises:
        InvalidDataTypeError, NonPositiveValueError, ImpossibleWeightError: 
            Based on the input value's validity and range.
    """
    def wrapper(*args, **kwargs):
        # Extract the first argument as weight (assumes positional arg)
        if not args or len(args[0]) == 1:
            raw_value = args[0][0]
        else:
            raise InvalidDataTypeError("Weight must be a single value.")

        try:
            normalized_weight = float(raw_value)
            
            # Check for non-positive values (including NaN and Inf if possible, 
            # though standard float checks usually suffice for this context)
            if not isinstance(normalized_weight, (int, float)) or \
               (isinstance(normalized_weight, bool)):  # Exclude booleans from numeric check
                raise InvalidDataTypeError(raw_value)

            if normalized_weight <= 0:
                raise NonPositiveValueError(normalized_weight)

            if normalized_weight > 1000.0:
                raise ImpossibleWeightError(normalized_weight)

        except (TypeError, ValueError):
            # Handle cases where conversion to float fails or type is wrong
            try:
                float(raw_value)
            except TypeError:
                pass
            
            raise InvalidDataTypeError(f"Cannot convert '{raw_value}' to a number.") from None
        
        return func(*args[1:], **kwargs)

    return wrapper

if __name__ == '__main__':
    # Hard-coded sample values for testing the decorator
    
    def process_weight(weight):
        """A simple function that processes weight."""
        print(f"Processing valid weight: {weight} kg")
    
    @validate_weight
    def test_valid_int():
        return 50.0

    @validate_weight
    def test_invalid_string():
        try:
            "not a number".process() # This will fail inside the decorator logic if passed directly, 
                                      # but here we simulate passing it to process_weight via wrapper context
            pass
        except InvalidDataTypeError as e:
            print(f"Caught expected error for string input: {e}")

    @validate_weight
    def test_zero():
        return 0.0
    
    @validate_weight
    def test_negative():
        return -15.0
    
    @validate_weight
    def test_impossible_large():
        return 2000.0 # Exceeds 1000 kg limit

    print("Running sample tests...")
    
    try:
        result = process_weight(75)
        print(f"Success with valid input: {result}")
    except Exception as e:
        print(f"Unexpected error in success case: {e}")

    # Simulating the decorator's behavior on invalid inputs by calling a dummy function 
    # that mimics how one would use it, since we can't easily inject args into process_weight directly without changing its signature.
    
    def dummy_wrapper(weight):
        return f"Result for weight: {weight}"

    @validate_weight
    def run_test_case(value, func=dummy_wrapper):
        try:
            res = func(value)
            print(f"Unexpected success with value {value}: {res}")
        except InvalidDataTypeError as e:
            print(f"Caught InvalidDataTypeError for input '{value}': {e}")
        except NonPositiveValueError as e:
            print(f"Caught NonPositiveValueError for input '{value}': {e}")
        except ImpossibleWeightError as e:
            print(f"Caught ImpossibleWeightError for input '{value}': {e}")

    # Test cases execution
    run_test_case(50)      # Should work (normalized to 50.0)
    
    try: 
        dummy_wrapper("abc")
    except Exception as e:
        print(f"Handled string error via decorator logic simulation above.") 

    # Directly testing the exceptions by creating a small helper that uses our decorated function
    @validate_weight
    def check_value(val):
        return val

    try:
        result = check_value(0)
    except NonPositiveValueError as e:
        print(f"Correctly caught zero input: {e}")

    try:
        result = check_value(-5.5)
    except NonPositiveValueError as e:
        print(f"Correctly caught negative input: {e}")

    try:
        result = check_value(1000.0) # Boundary case, should pass (<= 1000 is allowed? Task says "impossible", usually > limit)
                                   # Re-reading task: "throwing specific exceptions for ... impossible values". 
                                   # Usually weight <= 1000kg is possible in extreme cases but let's stick to strict > 1000 as impossible.
    except ImpossibleWeightError as e:
        print(f"Caught error for boundary input (if logic was >=): {e}")

    try:
        result = check_value(2500) # Definitely impossible
    except ImpossibleWeightError as e:
        print(f"Correctly caught large impossible weight: {e}")

    print("All tests completed.")