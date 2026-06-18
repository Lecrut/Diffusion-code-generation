def check_zero(func):
    """Decorator that checks if the result of the wrapped function is zero."""
    
    def wrapper(*args, **kwargs):
        # Call the original function to get its result
        result = func(*args, **kwargs)
        
        # Check if the result is equal to 0.0 (to handle both int and float zeros safely)
        if result == 0 or isinstance(result, bool) and not result:
            print("Result check passed: The value is zero.")
            
        return result
    
    return wrapper

def sample_function_1():
    """A simple function that returns a non-zero integer."""
    return 42

@check_zero
def sample_function_2():
    """A function whose result should be checked as potentially zero (but isn't)."""
    # Intentionally returning something else to demonstrate the check logic works on all results
    return "Hello, World!"

@check_zero
def sample_function_3():
    """A function that actually returns zero."""
    return 0.0

if __name__ == '__main__':
    print("Running Sample Function 1 (non-zero):")
    res = sample_function_1()
    
    print("\nRunning Sample Function 2 (string result):")
    res = sample_function_2()
    
    print("\nRunning Sample Function 3 (zero value):")
    res = sample_function_3()