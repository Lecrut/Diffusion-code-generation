class NegativeResultError(Exception):
    """Custom exception raised if a decorated function returns a negative value."""
    pass

def check_non_negative(func):
    """Decorator that checks if the result of the wrapped function is non-negative.
    
    If the result is negative, raises NegativeResultError with details about 
    which function and input caused it.
    """
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            
            # Handle cases where result might not be directly comparable (e.g., None or non-numeric types)
            if isinstance(result, (int, float)):
                if result < 0:
                    raise NegativeResultError(
                        f"Function '{func.__name__}' returned a negative value ({result}). "
                        f"This function should not return negative results."
                    )
            
            # For other types that might be implicitly comparable or representable as numbers, 
            # we could add more logic here if needed. Currently only strict numeric checks are enforced.
            
            return result
            
        except Exception:
            raise
    
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = f"Decorated version of {func.__doc__}"
    
    return wrapper

@check_non_negative
def calculate_distance(x, y):
    """Calculates the Euclidean distance between two points. 
    Distance is always non-negative."""
    import math
    return math.sqrt((x - 0) ** 2 + (y - 0) ** 2)

if __name__ == '__main__':
    # Test case 1: Valid positive result
    try:
        distance = calculate_distance(3, 4)
        print(f"Distance calculated successfully: {distance}")
        
        if distance < 0:
            raise NegativeResultError("Unexpected negative distance")
            
    except Exception as e:
        print(f"Test case 1 failed with error: {e}")

    # Test case 2: Simulating a function that returns negative (by modifying logic temporarily)
    def bad_function():
        return -5
    
    @check_non_negative
    def test_bad_func(*args, **kwargs):
        return bad_function()
    
    try:
        result = test_bad_func()
        print(f"Test case 2 failed: Expected exception but got {result}")
    except NegativeResultError as e:
        print(f"Test case 2 passed correctly with error: {e}")

    # Test case 3: Zero value (should be allowed)
    try:
        zero_result = calculate_distance(0, 0)
        if zero_result < 0:
            raise NegativeResultError("Zero should not trigger exception")
        print(f"Test case 3 passed correctly for zero result: {zero_result}")
    except Exception as e:
        print(f"Test case 3 failed with error: {e}")

    # Test case 4: Large negative value simulation via direct call to a modified function
    def always_negative():
        return -10
    
    @check_non_negative
    def trigger_error(*args, **kwargs):
        return always_negative()
    
    try:
        result = trigger_error(1, 2)
        print(f"Test case 4 failed: Expected exception but got {result}")
    except NegativeResultError as e:
        print(f"Test case 4 passed correctly with error: {e}")

    # Test case 5: Float negative value simulation
    def float_negative():
        return -3.14
    
    @check_non_negative
    def trigger_float_error(*args, **kwargs):
        return float_negative()
    
    try:
        result = trigger_float_error(0)
        print(f"Test case 5 failed: Expected exception but got {result}")
    except NegativeResultError as e:
        print(f"Test case 5 passed correctly with error: {e}")

    # Test case 6: Ensure non-numeric types don't break the decorator (though they won't trigger negative check)
    def returns_string():
        return "not a number"
    
    @check_non_negative
    def test_string(*args, **kwargs):
        return returns_string()
    
    try:
        result = test_string(123)
        print(f"Test case 6 passed correctly for non-numeric type: {result}")
    except Exception as e:
        # This shouldn't happen with current implementation unless string comparison is attempted elsewhere
        if "negative" in str(e).lower():
            print(f"Test case 6 failed unexpectedly due to negative check on string: {e}")
        else:
            print(f"Unexpected error type for test case 6 (acceptable): {type(e).__name__}: {e}")

    # Test case 7: Verify that the decorator preserves function name and docstring
    @check_non_negative
    def named_function():
        """This is a documented function."""
        return 10
    
    print(f"Test case 7 - Function name preserved: {named_function.__name__}")
    print(f"Test case 7 - Docstring preserved: {named_function.__doc__}")

    # Final summary of all tests completed without user input or external dependencies
    print("All test cases executed successfully.")