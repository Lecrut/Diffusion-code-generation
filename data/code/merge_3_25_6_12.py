def check_zero(func):
    """Decorator that checks if the result of a function is zero."""
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            if result == 0:
                print(f"Result {result} is zero.")
            return result
        except Exception as e:
            raise e
    return wrapper

@check_zero
def calculate_sum(a, b):
    """A sample function to test the decorator."""
    return a + b

if __name__ == '__main__':
    # Test case where result is zero
    print("Test 1 (Result should be zero):")
    res = calculate_sum(5, -5)
    
    # Test case where result is not zero
    print("\nTest 2 (Result should not be zero):")
    res2 = calculate_sum(3, 4)