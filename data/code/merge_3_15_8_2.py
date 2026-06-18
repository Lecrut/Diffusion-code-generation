import functools

# Predefined constant value to match against
TARGET_VALUE = 42

def match_checker(expected_value: int) -> callable:
    """
    A decorator factory that checks if a function's result matches 
    the expected_value provided. If it does, the original function is executed normally.
    
    Args:
        expected_value (int): The value to compare against the function's return value.

    Returns:
        callable: A wrapper function that executes the target function and verifies its output.
    """
    def decorator(func: callable) -> callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            
            # Check if the result matches the predefined constant value passed to match_checker
            if isinstance(result, int) and result == expected_value:
                return result
            
            else:
                raise ValueError(f"Function '{func.__name__}' returned {result}, but expected {expected_value}.")
        
        return wrapper
    
    return decorator

if __name__ == '__main__':
    # Sample function to be decorated
    def add_ten(x):
        """Adds ten to the input x."""
        return x + 10

    # Another sample function that will fail the check
    def subtract_five(y):
        """Subtracts five from the input y."""
        return y - 5

    print("Testing @match_checker with add_ten...")
    
    try:
        decorated_add = match_checker(42)(add_ten)
        output = decorated_add(32)
        print(f"Success! Result is {output}")
    except ValueError as e:
        print(f"Failed validation for add_ten. Error details: {e}")

    print("\nTesting @match_checker with subtract_five...")
    
    try:
        # We expect 47 from (52 - 5), so we check against 47 here to make it pass, 
        # or change the target in match_checker call if testing failure.
        decorated_sub = match_checker(47)(subtract_five)
        output = decorated_sub(52)
        print(f"Success! Result is {output}")
    except ValueError as e:
        print(f"Failed validation for subtract_five (if expected was 42). Error details: {e}")

    # Demonstration of failure case by checking against the original function's output which isn't 42
    try:
        decorated_fail = match_checker(42)(subtract_five)
        result = decorated_fail(57) # 57 - 5 = 52, should fail if target is 42
        print(f"Unexpected success for subtract_five with target 42. Result: {result}")
    except ValueError as e:
        print("Correctly caught failure case where result (52) != expected value (42).")

    # Test a function that actually returns the target value to ensure it works correctly
    def get_target():
        return TARGET_VALUE
    
    decorated_correct = match_checker(TARGET_VALUE)(get_target)
    final_result = decorated_correct()
    print(f"\nCorrect usage test: Function returned {final_result} which matches expected value.")