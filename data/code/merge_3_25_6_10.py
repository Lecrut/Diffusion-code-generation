def check_zero(func):
    """
    A decorator that wraps a function to automatically print 
    whether its result is zero upon execution.
    
    Args:
        func (callable): The original function to wrap.
        
    Returns:
        callable: The wrapped function with added side effect logic.
    """
    def wrapper(*args, **kwargs):
        # Execute the original function and capture the return value
        result = func(*args, **kwargs)
        
        # Check if the result is zero (handles int, float, etc.)
        if isinstance(result, (int, float)) and result == 0:
            print("Result is zero.")
        else:
            print(f"Result {result} is not zero.")
            
        return result
    
    return wrapper

if __name__ == '__main__':
    # Sample function to test the decorator
    def sample_function():
        """A simple function that returns 0."""
        x = 5 - 5
        y = float(1.0) * 0.0
        z = int(x + y)
        return z

    @check_zero
    def another_sample_func(a, b):
        """Another sample function returning a non-zero value."""
        return a + b
    
    # Execute the wrapped functions with hard-coded values
    result1 = sample_function()
    
    result2 = another_sample_func(3, 4)