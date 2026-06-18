class NegativeResultError(Exception):
    """Custom exception raised if a decorated function returns a negative value."""
    pass

def check_non_negative(func):
    """Decorator that checks if the result of the wrapped function is negative.
    
    If the returned value is less than zero, raises NegativeResultError with 
    details about which function failed and what it returned.
    Otherwise, proceeds normally.
    """
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            if isinstance(result, (int, float)) and result < 0:
                raise NegativeResultError(
                    f"Function {func.__name__} returned a negative value: {result}"
                )
            return result
        except Exception as e:
            # Re-raise any exceptions that were not related to the non-negative check
            if not isinstance(e, ValueError):  # Custom wrapper for clarity unless it's already an error we expect
                 raise

    return wrapper

@check_non_negative
def calculate_squares(numbers):
    """Calculates squares of numbers and returns their sum.
    
    Args:
        numbers (list): List of integers to square.
        
    Returns:
        int: Sum of squared values.
        
    Raises:
        NegativeResultError: If the result is negative (unlikely for sums of squares).
    """
    return sum(n * n for n in numbers)

@check_non_negative
def calculate_product(numbers):
    """Calculates product of numbers and returns its value.
    
    Args:
        numbers (list): List of integers to multiply.
        
    Returns:
        int or float: Product of values.
"""
    result = 1
    for n in numbers:
        result *= n
    return result

if __name__ == '__main__':
    # Test Case 1: Positive Result (should pass)
    try:
        res1 = calculate_squares([2, 3])
        print(f"Test 1 - Squares of [2, 3]: {res1}")
    except NegativeResultError as e:
        print(e)

    # Test Case 2: Negative Result (should raise exception)
    try:
        res2 = calculate_product([-2, 5])
        print(f"Test 2 - Product of [-2, 5]: {res2}")
    except NegativeResultError as e:
        print(e)

    # Test Case 3: Another Positive Result (should pass)
    try:
        res3 = calculate_squares([10])
        print(f"Test 3 - Square of [10]: {res3}")
    except NegativeResultError as e:
        print(e)