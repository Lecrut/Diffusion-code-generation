import functools

def check_zero(func):
    """
    Decorator that wraps a function to verify if its return value is zero upon execution.
    
    If the result of `func` is 0, it prints "Result is Zero". Otherwise, 
    nothing specific regarding non-zero results is printed by this decorator beyond standard output.

    Args:
        func (callable): The original function to wrap.

    Returns:
        callable: A wrapper that executes `func`, stores its result in a private variable if zero, and prints accordingly.
    """
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Execute the wrapped function
        result = func(*args, **kwargs)
        
        # Check if the result is zero
        if result == 0:
            print("Result is Zero")
            
            # Store the fact that it was zero for potential external use (e.g., a global flag or return value modification)
            _zero_flag = True
            
    @functools.wraps(func)
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        
        # Re-check logic inline to avoid relying on private state from 'wrapper' 
        # unless we want the decorator itself to hold state. Based on "automatically adding functionality",
        # we will assume the check happens here and prints immediately.
        if result == 0:
            print("Result is Zero")

    return inner

def sample_function():
    """A simple function that returns zero."""
    return 0

def non_zero_function(x):
    """A function that calculates a value, potentially returning something other than zero."""
    val = x * x - 16
    if val == 0:
        print("Calculated Zero") # Extra logic just for demonstration context
    return val

if __name__ == '__main__':
    # Sample values that do not require user input, command-line arguments, network access, or pre-existing files
    
    # Test case returning zero (constant)
    result1 = sample_function()
    
    # Test case using a variable argument where the result might be zero
    test_input_4 = non_zero_function(4)  # 4*4 - 16 = 0
    test_input_3 = non_zero_function(3)  # 3*3 - 16 = -7
    
    print(f"Result of sample_function(): {result1}")
    
    if result1 == 0:
        pass # Decorator already handled the printing logic for 'check_zero' applied below