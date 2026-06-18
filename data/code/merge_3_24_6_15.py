class NegativeResultError(Exception):
    """Custom exception raised when a function returns a negative result."""
    pass

def check_non_negative(func):
    """
    Decorator that checks if the decorated function's return value is non-negative.
    
    If the returned value is less than zero, raises NegativeResultError with details.

    Args:
        func (callable): The function to decorate.
        
    Returns:
        callable: A wrapped version of the original function.
    """
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result < 0:
            raise NegativeResultError(f"Function '{func.__name__}' returned a negative value: {result}")
        return result
    return wrapper

@check_non_negative
def calculate_sum(a, b):
    """Calculates the sum of two numbers."""
    return a + b

if __name__ == '__main__':
    # Test case 1: Returns positive (should pass)
    try:
        result = calculate_sum(5, 3)
        print(f"Test 1 passed. Result: {result}")
    except NegativeResultError as e:
        print(f"Test 1 failed with error: {e}")

    # Test case 2: Returns negative (should raise exception)
    try:
        result = calculate_sum(-5, -3)
        print(f"Test 2 passed. Result: {result}")
    except NegativeResultError as e:
        print("Test 2 correctly raised an error.")

    # Test case 3: Returns zero (should pass)
    try:
        result = calculate_sum(-5, 5)
        if result >= 0:
            print(f"Test 3 passed. Result: {result}")
        else:
            print("Test 3 failed unexpectedly.")
    except NegativeResultError as e:
        print(f"Test 3 raised error (expected None check): {e}")

    # Test case 4: Explicit negative return via custom helper to ensure robustness
    @check_non_negative
    def always_negative():
        return -10
    
    try:
        result = always_negative()
    except NegativeResultError as e:
        print(f"Test 4 correctly raised an error for always negative function.")

    # Test case 5: Zero is acceptable (should pass)
    @check_non_negative
    def returns_zero():
        return 0