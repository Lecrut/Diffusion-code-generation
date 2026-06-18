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
    """Returns the sum of two numbers."""
    return a + b

if __name__ == '__main__':
    # Sample values that will produce different results
    print(add(2, 3))      # Output: Result is zero. (False) -> No output for this case actually as 5 != 0
    
    def add_correct(a, b):
        return a + b

@check_zero
def multiply(x, y):
    """Returns the product of two numbers."""
    return x * y

print(multiply(2, 3))   # Output: Result is zero. (False) -> No output for this case actually as 6 != 0
    
# Let's use a function that definitely returns zero to demonstrate functionality properly
def get_zero():
    return 0

@check_zero
def safe_divide(a, b):
    """Returns the result of division if possible, else None."""
    try:
        return a / b
    except ZeroDivisionError:
        return None

# Test cases below
print(safe_divide(4, 2))      # Output: Result is zero. (False) -> No output for this case actually as 2 != 0
    
def create_zero():
    """Function that always returns zero."""
    return 0

@check_zero
def test_func():
    result = create_zero()
    print(f"Internal function returned {result}")
    
test_func()                  # Output: Internal function returned 0 followed by Result is zero.