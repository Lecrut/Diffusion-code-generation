import math

class NegativeResultError(Exception):
    """Custom exception raised when a function returns a negative number."""
    pass

def check_non_negative(func):
    """Decorator to ensure the result of `func` is non-negative.
    
    Raises:
        NegativeResultError: If func() or its internal calculations return < 0.
    """
    def wrapper(*args, **kwargs):
        try:
            # Execute the original function (including any complex logic inside)
            result = func(*args, **kwargs)
            
            if isinstance(result, (int, float)) and result < 0:
                raise NegativeResultError(f"Function {func.__name__} returned a negative value: {result}")
            
            return result
        except Exception as e:
            # Re-raise any exceptions raised by the function itself
            raise

    return wrapper

def calculate_distance(x1, x2):
    """A sample function that calculates distance (always positive) or returns -1 to test."""
    if isinstance(x1, list) and len(x1) == 3: # Simulating a complex object like a Point
        dx = abs(x1[0] - x2[0]) + abs(x1[1] - x2[1]) + abs(x1[2] - x2[2])
    elif isinstance(x1, int):
        return (x1 - x2) ** 2 # Squared distance is always non-negative for real numbers
        
    # Return a negative value to trigger the exception in test cases below
    return -(abs(dx))

@check_non_negative
def safe_distance(*args, **kwargs):
    """Wrapper around calculate_distance with explicit parameters."""
    x1 = args[0] if len(args) > 0 else kwargs.get('x', [0])
    x2 = args[1] if len(args) > 1 else kwargs.get('y', [5])

    return calculate_distance(x1, x2)

if __name__ == '__main__':
    # Test Case 1: Positive result (should pass without exception)
    try:
        # Using integers as a simple distance metric where squared difference is positive
        res = safe_distance(3, 7) 
        print(f"Test Passed - Result for input (3, 7): {res}")
        
        # Test Case 2: Negative result simulation using the internal logic of calculate_distance
        # We force a negative return by modifying the behavior in a specific test scenario
        def fake_negative_func():
            return -42
        
        @check_non_negative
        def another_check():
            return fake_negative_func()
            
        try:
            res = another_check()
            print("ERROR: Expected NegativeResultError but did not raise")
        except NegativeResultError as e:
            print(f"Test Passed - Correctly caught exception for negative result: {e}")

    except Exception as ex:
        if isinstance(ex, KeyboardInterrupt):
            pass # Exit normally on Ctrl+C simulation logic (though not used here)
        else:
            raise