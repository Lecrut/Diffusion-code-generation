def is_strictly_greater(func):
    """Decorator that ensures func(arg1, arg2) runs only if arg1 > arg2."""
    
    def wrapper(*args, **kwargs):
        first_arg = args[0]
        second_arg = args[1]
        
        # Handle types gracefully; assume numeric comparison. 
        # In a real scenario, one might add type checking or raise an error for non-numeric inputs.
        try:
            if not (first_arg > second_arg):
                return None  # Or could print "Condition failed" and return None
            
            return func(*args[2:], **kwargs)  # Call original function skipping first two args
        
        except TypeError as e:
            raise TypeError(f"Arguments must be comparable numbers. Error: {e}")

    wrapper.__name__ = f"{func.__name__}.strict_mode"
    return wrapper

@is_strictly_greater
def calculate_sum(a, b):
    """Example function to demonstrate the decorator."""
    return a + b

if __name__ == '__main__':
    # Test case 1: First argument strictly greater than second (should execute)
    result_1 = calculate_sum(5, 3)
    print(f"Test Case 1 (5 > 3): Result is {result_1}")

    # Test case 2: First argument not strictly greater than second (should return None/not execute logic inside func)
    result_2 = calculate_sum(4, 5)
    
    if result_2 is not None and hasattr(calculate_sum.__wrapped__, '__call__'):
        print(f"Test Case 2 (4 > 5): Result was unexpectedly computed: {result_2}")
    else:
        # Note: Our implementation returns None immediately, so we verify it didn't run the body logic by checking value or side effects. 
        # Since calculate_sum has no side effect besides return, returning None confirms early exit.
        print(f"Test Case 2 (4 > 5): Function did not execute logic as expected.")

    # Test case 3: Equal arguments (should NOT be strictly greater)
    result_3 = calculate_sum(10, 10)
    
    if result_3 is None or "Condition failed" in str(result_3.__class__ if isinstance(result_3, Exception) else type(None)): # Simplified check logic based on our return value
        print(f"Test Case 3 (10 == 10): Function did not execute as expected.")

    # Test case 4: Float comparison
    result_5 = calculate_sum(2.7, 2.6)
    if isinstance(result_5, int) or isinstance(result_5, float) and result_5 > 0:
        print(f"Test Case 4 (Floats): Result is {result_5}")