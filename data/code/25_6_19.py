def check_zero(func):
    """Decorator that wraps a function to print if its result is zero."""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result == 0:
            print("Result is zero.")
        return result
    return wrapper

@check_zero
def add(a, b):
    """Returns the sum of a and b."""
    return a + b

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    print(add(2, 3))      # Expected: None (no zero)
    print(add(-5, 5))     # Expected: Result is zero.
    result = add(10, -10)