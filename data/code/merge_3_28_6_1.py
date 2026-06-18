def is_strictly_greater(func):
    """Decorator that ensures func executes only if its first argument 
    is strictly greater than its second argument."""
    
    def wrapper(*args, **kwargs):
        # Extract the first two positional arguments for comparison
        if len(args) < 2:
            raise TypeError("is_strictly_greater requires at least two positional arguments")
        
        a = args[0]
        b = args[1]
        
        if not (a > b):
            return None
        
        # Execute the original function with remaining arguments passed through
        return func(*args, **kwargs)
    
    wrapper.__name__ = func.__name__
    return wrapper

if __name__ == '__main__':
    def add(x, y):
        """Simple addition function."""
        return x + y

    # Test cases with hard-coded values
    
    # Case 1: First argument strictly greater than second (should execute)
    result_1 = is_strictly_greater(add)(5, 3)
    
    # Case 2: First argument equal to second (should not execute, returns None)
    result_2 = is_strictly_greater(add)(4, 4)
    
    # Case 3: First argument less than second (should not execute, returns None)
    result_3 = is_strictly_greater(add)(2, 8)

    print(f"Result of add(5, 3): {result_1}")   # Expected: 8
    print(f"Result of add(4, 4): {result_2}")   # Expected: None (condition failed)
    print(f"Result of add(2, 8): {result_3}")   # Expected: None (condition failed)