import functools

# Predefined constant value to match against
TARGET_VALUE = 42

def match_checker(expected_value: int):
    """
    Decorator that checks if a function's return value matches expected_value.
    
    If the result does not match, it raises an AssertionError with details about 
    what was returned instead of the expected value.
    
    Args:
        expected_value (int): The constant value to compare against.
        
    Returns:
        A decorator that wraps a function and enforces this check on its return value.
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            
            if result != expected_value:
                raise AssertionError(
                    f"Function '{func.__name__}' returned {result}, "
                    f"but the value must match {expected_value}."
                )
                
            return result
        
        return wrapper
    
    return decorator

if __name__ == '__main__':
    # Sample function that returns a specific integer
    def add_ten(x: int) -> int:
        """Returns x + 10"""
        return x + 10

    # Function returning the target value (42), which should pass without error
    def get_target() -> int:
        return TARGET_VALUE
    
    # Function that returns a different value, expected to raise AssertionError
    def wrong_return(x: int) -> int:
        return x * 10

    print("Running tests with @match_checker...")

    try:
        decorated_add = match_checker(52)(add_ten)
        result = decorated_add(42)
        assert result == 52, "Test failed"
        print(f"✓ Test passed for add_ten(42): returned {result}")
        
    except AssertionError as e:
        print(f"✗ Unexpected failure in first test: {e}")

    try:
        decorated_get = match_checker(TARGET_VALUE)(get_target)
        result = decorated_get()
        assert result == TARGET_VALUE, "Test failed for get_target"
        print(f"✓ Test passed for get_target(): returned {result}")
        
    except AssertionError as e:
        print(f"✗ Unexpected failure in second test: {e}")

    try:
        # This should fail because 420 != 42
        decorated_wrong = match_checker(TARGET_VALUE)(wrong_return)
        result = decorated_wrong(4.2)  # Using float to ensure int mismatch if needed, though logic holds for any type diff
        print(f"✗ Test failed: expected AssertionError but got {result}")
    except AssertionError as e:
        print(f"✓ Expected failure caught correctly: {e}")

    print("All tests completed.")