import functools

# Predefined constant value to match against
TARGET_VALUE = 42

def match_checker(expected_value: int):
    """
    Decorator that checks if a function's return value matches expected_value.
    
    Args:
        expected_value (int): The integer value the decorated function must return.

    Returns:
        A decorator factory returning a wrapper function.
        
    Raises:
        AssertionError: If the result of the wrapped function does not match expected_value.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            
            # Check if the result matches the predefined constant value passed to the decorator
            assert result == expected_value, f"Function returned {result}, but expected {expected_value}"
            
            return result
        
        return wrapper
    
    return decorator

if __name__ == '__main__':
    # Sample function that returns 42
    @match_checker(TARGET_VALUE)
    def get_number():
        """Returns the target number."""
        return TARGET_VALUE

    # Call the decorated function to verify it works correctly
    result = get_number()
    
    print(f"Function returned: {result}")
    
    if result == TARGET_VALUE:
        print("SUCCESS: The decorator check passed.")
    else:
        print("FAILURE: The decorator check failed.")