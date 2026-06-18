class ResultNegativeError(Exception):
    """Custom exception raised when a decorated function returns a negative value."""
    pass

def result_negative_checker(func):
    """Decorator that checks if the result of the wrapped function is negative and raises ResultNegativeError otherwise.

    Args:
        func (callable): The function to decorate.

    Returns:
        callable: A wrapper around `func` with additional validation logic.
    """
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            
            # Check if the result is negative (works for numbers that can be compared to 0)
            # If it's a string or other non-numeric type, this comparison will raise TypeError naturally.
            # We only care about numeric negativity here based on typical use cases.
            if isinstance(result, (int, float)) and result < 0:
                raise ResultNegativeError(f"Result of {func.__name__} is negative ({result}).")
            
            return result
        except Exception as e:
            # If the original function raised an error unrelated to negativity, propagate it.
            if not isinstance(e, ResultNegativeError):
                raise
    return wrapper

if __name__ == '__main__':
    @result_negative_checker
    def calculate_square(x):
        """Returns the square of a number."""
        return x * x

    # Test case 1: Positive result (should pass)
    try:
        val1 = calculate_square(5)
        print(f"Test 1 passed. Result is positive ({val1}).")
    except Exception as e:
        print(f"Unexpected error in Test 1: {e}")

    # Test case 2: Negative result (should raise exception)
    try:
        val2 = calculate_square(-3)
        print("Test 2 failed. Expected ResultNegativeError but got no exception.")
    except ResultNegativeError as e:
        print(f"Test 2 passed correctly. Exception raised with message: {e}")

    # Test case 3: Zero result (should pass, zero is not negative)
    try:
        val3 = calculate_square(0)
        if val3 == 0:
            print("Test 3 passed. Result is zero ({val3}).")
        else:
            print(f"Unexpected value in Test 3: {val3}")
    except Exception as e:
        print(f"Unexpected error in Test 3: {e}")

    # Additional manual test with a negative number directly for clarity if needed, 
    # though the decorator handles it inside calculate_square.
    
    @result_negative_checker
    def get_value(n):
        """A function that might return different values."""
        import math
        result = -n * 2 + n ** 0.5
        
        print(f"Raw calculation for input {n}: {-n*2 + n**0.5}")

    try:
        res = get_value(1) # Should be negative (-1 + sqrt(1)) -> roughly -0 or slightly pos/neg depending on float precision, let's pick clear case
                # Let's use a clearer example for the test below to ensure negativity is obvious without complex math logic in decorator scope.
        print(f"Result of get_value(5): {res}")
    except ResultNegativeError as e:
        print(f"Catch handled negative result from get_value: {e}")