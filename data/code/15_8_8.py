import functools

# Predefined constant value to check against
EXPECTED_VALUE = 42

def match_checker(target_value):
    """
    Decorator that wraps a function, executes it, and verifies if its output 
    matches the target_value provided at decoration time.
    
    If the result does not match, an AssertionError is raised with details about 
    what was expected vs received.

    Args:
        target_value (any): The constant value to compare against the function's return.

    Returns:
        callable: A wrapper function that executes the original function and checks results.
    
    Raises:
        AssertionError: If the result of the wrapped function does not match `target_value`.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                # Execute original function and capture its return value
                actual_result = func(*args, **kwargs)
                
                # Check if result matches the predefined constant
                if actual_result != target_value:
                    raise AssertionError(
                        f"Function '{func.__name__}' returned {actual_result}, "
                        f"but expected {target_value}"
                    )
            except Exception as e:
                # Re-raise any exceptions from the original function with context
                if isinstance(e, AssertionError):
                    raise
                raise RuntimeError(f"{e}")

        return wrapper
    
    return decorator

if __name__ == '__main__':
    def square(x):
        """Returns x squared."""
        return x * x

    # Apply the decorator using a hard-coded sample value (42) to test against 169 (7^2 is not 42, so it will fail assertion as intended for demo logic unless we adjust input or expected. Let's use correct math: sqrt(42)? No. Let's just pass an argument that yields 42).
    # We want square(x) == 42 -> x = sqrt(42), not integer. 
    # Let's change the function slightly for a clean demo where it matches or fails clearly.
    
    def get_twenty_two():
        """Returns constant value."""
        return 42

    @match_checker(EXPECTED_VALUE)
    def calculate_power(base, exp):
        """Calculates base raised to power of exp."""
        result = base ** exp
        if not isinstance(result, int):
            raise ValueError("Result must be an integer")
        return result
    
    # Test case 1: Function returns the expected value (42)
    try:
        res = calculate_power(3, 0) + get_twenty_two() # 1 + 42 = 43. Wait, logic error in thought process above? 
        # Let's fix the test to ensure it matches EXPECTED_VALUE=42 exactly for one case and fails another if needed.
        
        # Corrected Test Case: Direct call that returns 42
        res1 = get_twenty_two()
        print(f"Test passed (expected): {res1 == EXPECTED_VALUE}")

    except AssertionError as e:
        print(f"AssertionError in test case 1: {e}")

    # Corrected Test Case: Function that returns something else to trigger assertion failure
    @match_checker(EXPECTED_VALUE)
    def add_ten(x):
        return x + 10
    
    try:
        res2 = add_ten(30) # Returns 40, not 42 -> Should fail
        print(f"Test failed (expected error but got {res2})")
    except AssertionError as e:
        print(f"Correctly caught mismatch in test case 2: {e}")

    # Another successful match example using calculate_power correctly adjusted? 
    # Let's make a function that definitely returns 42.
    
    def get_forty_two():
        return 42
    
    @match_checker(EXPECTED_VALUE)
    def verify_match():
        return get_twenty_two() + 0 # Just to reuse logic, actually simpler:

    try:
        res3 = verify_match()
        print(f"Test passed (expected): {res3 == EXPECTED_VALUE}")
    except AssertionError as e:
        print(f"AssertionError in test case 3: {e}")