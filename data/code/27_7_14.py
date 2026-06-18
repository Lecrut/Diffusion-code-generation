def check_not_equal(threshold):
    """
    A decorator that wraps a function to ensure its result is not equal 
    to the specified threshold value. If it equals the threshold, 
    an exception is raised.
    
    Args:
        threshold (any type): The value that the wrapped function's return 
                              should not be equal to.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result == threshold:
                raise ValueError(f"Result {result} is equal to the forbidden threshold {threshold}.")
            return result
        return wrapper
    return decorator

import functools

if __name__ == '__main__':
    # Define a simple function that calculates difference between two numbers
    def calculate_difference(a, b):
        """Returns the absolute difference between a and b."""
        return abs(a - b)

    # Apply the decorator to check if result is not 0 (meaning inputs differ)
    @check_not_equal(threshold=0)
    def are_different(x, y):
        """Wrapper that checks if x and y are different using calculate_difference."""
        diff = calculate_difference(x, y)
        return f"The values {x} and {y} have a difference of {diff}. They differ."

    # Sample execution with hard-coded values
    result1 = are_different(5, 3)
    print(result1)

    try:
        # This should trigger the check because abs(4-4) == 0
        result2 = are_different(4, 4)
    except ValueError as e:
        print(f"Error detected (as expected): {e}")