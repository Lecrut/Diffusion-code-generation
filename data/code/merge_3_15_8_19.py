import functools

# Predefined constant value to match against
TARGET_VALUE = 42

def match_checker(expected_value: int) -> callable:
    """
    Decorator that checks if a function's return value matches the expected_value.
    
    Args:
        expected_value (int): The integer value that the decorated function must return.
        
    Returns:
        A decorator factory returning a wrapper function.
    """

    def decorator(func: callable) -> callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            
            # Check if the result matches the predefined constant value passed to match_checker
            if result != expected_value:
                raise AssertionError(
                    f"Function {func.__name__} returned {result}, "
                    f"but it was expected to return {expected_value}"
                )
            
            return result
        
        return wrapper
    
    return decorator

if __name__ == '__main__':
    # Sample function that returns the target value
    def add_ten(x: int) -> int:
        """Returns x + 10"""
        return x + 10

    # Apply the match_checker decorator with TARGET_VALUE (42) as expected result
    @match_checker(expected_value=TARGET_VALUE)
    def correct_function() -> int:
        """This function is designed to return exactly 42"""
        return 42
    
    # Another sample function that returns a different value, should raise AssertionError when decorated
    @match_checker(expected_value=TARGET_VALUE)
    def incorrect_function() -> int:
        """This function incorrectly returns 50 instead of 42"""
        return 50

    print("Running correct_function...")
    try:
        result = correct_function()
        print(f"Success! Result is {result}")
    except AssertionError as e:
        print(f"Error in correct_function: {e}")

    print("\nRunning incorrect_function (should fail)...")
    try:
        result = incorrect_function()
        print(f"Unexpected success with result {result}")
    except AssertionError as e:
        print(f"Expected error occurred for incorrect_function: {e}")