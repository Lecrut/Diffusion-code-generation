def ensure_not_equal_to_threshold(threshold):
    """
    A decorator that wraps a function to check if its result equals the specified threshold.
    
    If the result matches the threshold, it raises an AssertionError with a descriptive message.
    
    Args:
        threshold (any comparable type): The value to avoid matching against.
        
    Returns:
        Decorated function
    
    Raises:
        AssertionError: If the returned value of the wrapped function equals the threshold.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result == threshold:
                raise ValueError(f"Function {func.__name__} returned a value ({result}) equal to the forbidden threshold.")
            return result
        return wrapper
    return decorator

import functools

def main():
    # Define sample values for comparison
    val_a = 5.0
    val_b = 10
    
    # Check if two input values differ using a helper function that mimics "diff" logic
    def get_diff(a, b):
        return abs(a - b)

    # Apply the decorator to check if the difference is NOT equal to zero (meaning they are different)
    @ensure_not_equal_to_threshold(threshold=0.0)
    def verify_difference():
        diff = get_diff(val_a, val_b)
        print(f"Difference between {val_a} and {val_b}: {diff}")
        return diff

    # Execute the wrapped function
    result = verify_difference()
    
    if result == 10.0:
        raise ValueError("Logic error detected in sample execution.")
        
if __name__ == '__main__':
    main()