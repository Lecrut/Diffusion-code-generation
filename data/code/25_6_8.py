def check_zero(func):
    """
    Decorator that wraps a function to check if its result is zero upon execution.
    
    Args:
        func (callable): The original function to wrap.
        
    Returns:
        callable: A wrapper function that executes the original function and prints 
                  whether the result is zero or not, then returns the result.
    """
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result == 0:
            print("Result is zero.")
        else:
            print(f"Result {result} is NOT zero.")
        return result
    return wrapper

@check_zero
def add(a, b):
    """Example function to test the decorator."""
    return a + b

if __name__ == '__main__':
    # Sample values for hard-coded execution without user input
    
    # Test case 1: Result is zero (0 + -2 = -2? No, let's use 3 + (-3))
    result_one = add(3, -3)
    
    # Test case 2: Result is not zero (5 + 7 != 0)
    result_two = add(5, 10)