def check_truth(condition):
    """
    A decorator that wraps a function to ensure it only executes 
    if 'condition' is True. If condition is False, the wrapped 
    function will not be called and returns None instead.
    
    Args:
        condition (bool or any truthy value): The condition passed at decoration time.
        
    Returns:
        A decorator that wraps a target function. When invoked with this decorator,
        it checks 'condition' before executing the wrapped function. If True, 
        executes normally; if False, returns None without calling the original function.
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        
        # Check condition at decoration time (when this module is imported/loaded), not runtime per call
        if condition:
            return wrapper
        
        def no_op_wrapper(*args, **kwargs):
            """Wrapper that does nothing and returns None when condition was False."""
            pass
        
        return no_op_wrapper

    # Since decorators are applied at import time in Python for simple static conditions,
    # we need to handle the logic differently if 'condition' is evaluated once.
    # However, standard decorator syntax evaluates arguments immediately upon application.
    # To make this work as a reusable pattern where condition might be dynamic later (though not typical),
    # let's assume the user passes a boolean value directly when applying it here in main or similar context.
    
    return wrapper

# Correct approach for static decoration: The decorator itself must evaluate 'condition' 
# immediately upon being called with an argument, but that requires redefining behavior based on arg.
# Let's redefine slightly to fit the requirement of "wraps a function and ensures... if condition is True".

def check_truth(condition):
    def decorator(func):
        # Evaluate condition now (at decoration time)
        if not condition:
            return lambda *args, **kwargs: None
        
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        
        return wrapper
    
    return decorator

if __name__ == '__main__':
    # Example usage with hard-coded sample values
    
    # Define a simple function to test
    def add_numbers(a, b):
        """Adds two numbers and returns the result."""
        return a + b
    
    # Test Case 1: Condition is True -> Function should execute
    print("Test Case 1 (Condition = True)")
    decorated_add_true = check_truth(True)(add_numbers)
    
    try:
        result_1 = decorated_add_true(5, 3)
        if isinstance(result_1, int):
            print(f"Success: Function executed. Result: {result_1}")
        else:
            print("Error: Unexpected return type")
    except Exception as e:
        print(f"Unexpected error in Test Case 1: {e}")

    # Test Case 2: Condition is False -> Function should NOT execute (return None)
    print("\nTest Case 2 (Condition = False)")
    decorated_add_false = check_truth(False)(add_numbers)
    
    try:
        result_2 = decorated_add_false(10, 20)
        if isinstance(result_2, type(None)):
            print("Success: Function did not execute. Returned None.")
        else:
            print(f"Error: Expected None but got {result_2}")
    except Exception as e:
        # If an exception is raised (e.g., from the lambda returning something unexpected), catch it
        if "NoneType" in str(type(e)) or result_2 == 30: 
            print(f"Note: In some environments, a no-op might behave differently. Result was {result_2}")

    # Test Case 3: Condition is non-empty string (truthy) -> Function should execute
    print("\nTest Case 3 (Condition = 'hello' - Truthy)")
    decorated_add_truthy = check_truth("hello")(add_numbers)
    
    try:
        result_3 = decorated_add_truthy(1, 2)
        if isinstance(result_3, int):
            print(f"Success: Function executed. Result: {result_3}")
        else:
            print("Error: Unexpected return type")
    except Exception as e:
        print(f"Unexpected error in Test Case 3: {e}")

    # Summary of results
    print("\n--- Execution Summary ---")
    if result_1 == 8 and result_2 is None and isinstance(result_3, int) and result_3 == 3:
        print("All tests passed successfully.")
    else:
        print(f"Results check failed. Expected [8, None, 3], got [{result_1}, {result_2}, {result_3}]")