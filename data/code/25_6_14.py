def check_zero(func):
    """
    A decorator that wraps a function to automatically print whether its result is zero.
    
    Args:
        func (callable): The original function to wrap.
        
    Returns:
        callable: The wrapped function with added side-effect logic.
    """
    def wrapper(*args, **kwargs):
        # Execute the original function and capture the return value
        result = func(*args, **kwargs)
        # Check if the result is zero (handles 0, False for integers/bools as they are falsy but we specifically check == 0 or isinstance(result, int))
        # The prompt asks to "check if the result ... is zero". 
        # We will use strict equality with 0.
        print(f"Result of {func.__name__}: {result}")
        print(f"Is result zero? {result == 0}")
        return result
    
    return wrapper

if __name__ == '__main__':
    def add(a, b):
        """Returns the sum of a and b."""
        return a + b
    
    def subtract(x, y):
        """Subtracts x from y."""
        return y - x
    
    # Sample execution with hard-coded values that might result in zero or non-zero
    print("--- Testing add function ---")
    wrapped_add = check_zero(add)
    res1 = wrapped_add(2, 3)   # Result: 5 (not zero)
    
    print("\n--- Testing subtract function ---")
    wrapped_subtract = check_zero(subtract)
    res2 = wrapped_subtract(5, 5)      # Result: 0 (is zero)
    res3 = wrapped_subtract(10, 4)     # Result: 6 (not zero)

    print("\n--- Testing with a function that always returns zero ---")
    def get_zero():
        return 0
    
    wrapped_get_zero = check_zero(get_zero)
    res4 = wrapped_get_zero()   # Result: 0 (is zero)