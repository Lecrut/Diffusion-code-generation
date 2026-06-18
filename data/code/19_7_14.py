def check_truth(condition):
    """
    A decorator that wraps a function to ensure it only executes 
    if the provided condition is True.
    
    Args:
        condition (bool or any truthy value): The condition checked before execution.
        
    Returns:
        Decorated function wrapped with conditional logic.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            if not bool(condition):
                print(f"Function '{func.__name__}' skipped because {condition} is falsy.")
                return None
            
            # Execute the original function and capture its result
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as e:
                print(f"Error executing {func.__name__}: {e}")
                raise
        
        wrapper.__name__ = f"{condition}_{func.__name__}"  # Optional naming convention
        return wrapper
    
    return decorator

# Example usage within the main block if needed, but decorators are applied at definition time.

if __name__ == '__main__':
    # Define a sample function to be wrapped
    def greet(name):
        """Returns a greeting message."""
        print(f"Hello, {name}!")
        return f"Greeting for {name}"

    # Apply the decorator with different conditions
    
    # Case 1: Condition is True (should execute)
    @check_truth(True)
    def run_greet_true(name):
        greet(name)
    
    # Case 2: Condition is False (should NOT execute)
    @check_truth(False)
    def run_greet_false(name):
        greet(name)

    print("--- Testing with True condition ---")
    result = run_greet_true("Alice")
    if result:
        print(f"Returned value: {result}")

    print("\n--- Testing with False condition (should be skipped) ---")
    # Note: This function will not execute due to the decorator logic
    
    # Case 3: Condition is a non-boolean truthy value (e.g., string "yes") - should still work in Python usually, 
    # but let's stick to boolean expectations for strictness or test with None which is falsy.
    
    @check_truth(None)
    def run_greet_none(name):
        greet(name)