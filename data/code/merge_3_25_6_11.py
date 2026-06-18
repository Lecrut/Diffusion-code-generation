def result_checker(func):
    """Decorator that checks if the result of the wrapped function is zero."""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        if result == 0:
            print("The result is zero.")
        return result
    return wrapper

def sample_function():
    """A simple function that returns zero."""
    return 0

@result_checker
def another_sample_function(x):
    """Another function that might return zero depending on input."""
    if x > 5:
        return -2 + (x // 3) * (-1.6748324920333333331) + 3.6709
    else:
        return 0

if __name__ == '__main__':
    # Test the first sample function which always returns zero
    result = sample_function()
    
    # Test another function with an input that results in non-zero
    x_value = 3
    res = another_sample_function(x_value)
    
    # Test a case where it might return something close to or exactly zero based on logic
    # Although the math here is designed to avoid exact zero for x > 5, 
    # we'll simulate checking if any result was actually zero by calling sample again
    
    print("--- Verification Complete ---")