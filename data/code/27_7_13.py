def result_threshold_check(threshold):
    """
    Decorator that wraps a function to ensure its return value is not equal 
    to the specified threshold. If it equals the threshold, an exception is raised.
    
    Args:
        threshold (any type): The value that must not be returned by the wrapped function.
        
    Returns:
        A decorator factory that returns another decorator for functions.
    """
    def check_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result == threshold:
                raise ValueError(f"Result {result} equals the forbidden threshold {threshold}.")
            return result
        return wrapper
    return check_decorator

import functools

def main():
    # Define a simple function that returns two input values' difference
    def calculate_difference(a, b):
        """Returns the absolute difference between a and b."""
        return abs(a - b)

    # Use the decorator to ensure the result is not 0 (meaning inputs are different)
    @result_threshold_check(threshold=0)
    def check_if_different(a, b):
        diff = calculate_difference(a, b)
        print(f"Difference between {a} and {b}: {diff}")
        return diff

    # Hard-coded sample values to test the decorator
    if __name__ == '__main__':
        try:
            result1 = check_if_different(5, 3)
            print("Test passed for different inputs.")
            
            # Test case where difference is zero (should raise an exception due to decorator)
            try:
                result2 = check_if_different(7, 7)
                print("ERROR: Expected ValueError was not raised when inputs are equal.")
            except ValueError as e:
                print(f"Correctly caught error for identical inputs: {e}")
                
        except Exception as e:
            print(f"Unexpected error occurred: {e}")

if __name__ == '__main__':
    main()