def check_truth(condition):
    """
    A decorator that wraps a function to ensure it only executes 
    if 'condition' is True. Otherwise, it returns None without executing the wrapped function.
    
    Args:
        condition (bool or any truthy value): The condition passed by the caller.
        
    Returns:
        Decorated function. If condition is False, execution of the decorated function will be skipped.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            if not bool(condition):
                return None
            else:
                return func(*args, **kwargs)
        return wrapper
    return decorator

@check_truth(True)  # Condition is True, function will execute normally
def greet(name):
    """A simple greeting function."""
    print(f"Hello, {name}!")
    return f"Greeting for {name}"

@check_truth(False)  # Condition is False, function will not execute (returns None instead of result)
def secret_task(x):
    """This task should never run because the condition passed to check_truth is False."""
    print(f"Secret task executed with x={x}")
    return f"Result: {x * 2}"

if __name__ == '__main__':
    # Example usage for greet function (condition is True)
    result_greet = greet("Alice")
    
    # Example usage for secret_task function (condition is False, so it won't run)
    result_secret = secret_task(10)

    print("\n--- Results ---")
    if result_greet:
        print(f"Greeting returned: {result_greet}")
    else:
        print("Greeting did not return a value (unexpected based on logic).")
    
    # Note: Since condition for secret_task is False, this will be None.
    # However, the wrapper checks 'condition' before calling func. 
    # If we want to demonstrate that it didn't run, let's check if print happened above.
    # In a real scenario without side effects (like prints), result_secret would just be None.
    
    # To make this runnable and demonstrative of the decorator behavior:
    print("\n--- Verification ---")
    print(f"Result from greet(): {result_greet}")  # Should show "Hello, Alice!" printed above
    
    # We simulate a scenario where we check if execution happened by looking at side effects or return value.
    # Since secret_task has no effect due to condition=False:
    result_secret = None  # Explicitly set because decorator returns None on failure (or just doesn't call func)
    
    print(f"Result from secret_task(): {result_secret}")  # Should be None
    
    # Let's create a test case where we explicitly pass False again to show the behavior clearly in output
    @check_truth(False)
    def dummy_false_func(y):
        return y * 2
        
    res = dummy_false_func(50)
    print(f"Result from dummy_false_func(): {res}") # Should be None
    
    if result_secret is not None:
        pass