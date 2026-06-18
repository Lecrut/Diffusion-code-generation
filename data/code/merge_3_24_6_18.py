class NegativeResultError(Exception):
    """Custom exception raised if a decorated function returns a negative value."""
    pass

def check_non_negative(func):
    """Decorator that checks if the result of the wrapped function is non-negative.
    
    If the result is negative, raises NegativeResultError with details about the failure.
    Otherwise, proceeds normally and returns the original result.
    """
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            
            if isinstance(result, (int, float)) and result < 0:
                raise NegativeResultError(f"Function {func.__name__} returned a negative value: {result}")
                
            return result
        except Exception as e:
            # Re-raise any exceptions that occurred during function execution
            raise

    return wrapper

if __name__ == '__main__':
    def calculate_square(x):
        """Sample function that squares an input."""
        return x * x
    
    @check_non_negative
    def get_sum(a, b):
        """Sample function that returns the sum of two numbers. 
           Used to test negative results via a helper logic below."""
        # Normally this is positive for most inputs, but we'll override behavior in tests if needed
        return a + b
    
    @check_non_negative
    def get_product(a, b):
        """Sample function that returns the product of two numbers. 
           Used to test negative results when multiplying by -1."""
        return a * b

    # Test Case 1: Positive result (should pass)
    try:
        res = calculate_square(5)
        print(f"Test 1 Passed: {res}")
    except NegativeResultError as e:
        print(f"Test 1 Failed with error: {e}")

    # Test Case 2: Using get_sum to ensure positive result (should pass)
    try:
        res = get_sum(3, 4)
        print(f"Test 2 Passed: {res}")
    except NegativeResultError as e:
        print(f"Test 2 Failed with error: {e}")

    # Test Case 3: Using get_product to generate negative result (should fail)
    try:
        res = get_product(5, -10)
        print(f"Test 3 Unexpectedly Passed: {res}")
    except NegativeResultError as e:
        print(f"Test 3 Correctly Raised Exception: {e}")

    # Test Case 4: Direct negative number simulation via a custom helper decorated function
    def get_negative():
        return -5
    
    @check_non_negative
    def trigger_error():
        """Function that always returns a negative value to test the decorator."""
        return get_negative()
    
    try:
        res = trigger_error()
        print(f"Test 4 Unexpectedly Passed: {res}")
    except NegativeResultError as e:
        print(f"Test 4 Correctly Raised Exception: {e}")

    # Test Case 5: Zero result (should pass, zero is not negative)
    def get_zero():
        return 0
    
    @check_non_negative
    def test_zero():
        """Function that returns zero."""
        return get_zero()
    
    try:
        res = test_zero()
        print(f"Test 5 Passed (Zero allowed): {res}")
    except NegativeResultError as e:
        print(f"Test 5 Failed unexpectedly with error: {e}")