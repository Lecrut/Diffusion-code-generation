import functools

def check_threshold(threshold):
    """
    A decorator that wraps a function to ensure its result is not equal 
    to the specified threshold value. If the condition fails, it raises an error.
    
    Args:
        threshold (any comparable type): The value to compare against.
        
    Returns:
        Decorated function with added validation logic.
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result == threshold:
                raise ValueError(f"Result {result} is equal to the forbidden threshold.")
            return result
        return wrapper
    return decorator

def are_different(a, b):
    """A simple function that returns True if two values differ."""
    return a != b

if __name__ == '__main__':
    # Sample test case 1: Values should be different (True)
    threshold = False
    
    @check_threshold(threshold)
    def check_diff(val_a, val_b):
        return are_different(val_a, val_b)
    
    try:
        result_1 = check_diff(5, 3)
        print(f"Test 1 (values differ): {result_1}")
        
        # Sample test case 2: Values should be different (True), but threshold is False so it passes
        @check_threshold(True)
        def check_same(val_a, val_b):
            return are_different(val_a, val_b)
            
        result_2 = check_same(5, 3)
        print(f"Test 2 (values differ with True threshold): {result_2}")

    except ValueError as e:
        print(f"Error caught: {e}")