import functools

def verify_first_argument(min_value: int = 100):
    """
    Decorator that verifies if the first argument passed to a function is greater than min_value.
    
    Args:
        min_value (int): The threshold value for comparison. Default is 100.
        
    Returns:
        A decorator function that wraps another function and raises ValueError 
        if the condition is not met.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Check if there are any arguments (excluding self in methods usually, but here we check all args as per task description context of 'first argument')
            # The task says "first argument passed", so we take the first positional arg.
            if len(args) > 0:
                first_arg = args[0]
                try:
                    int_val = int(first_arg)
                    if not (int_val > min_value):
                        raise ValueError(f"First argument {first_arg} is not greater than {min_value}")
                except TypeError as e:
                    # If the first arg cannot be converted to int, we can't perform numeric comparison easily without specific logic. 
                    # Assuming for this task that arguments are expected to be comparable or integers based on "greater than" context.
                    raise ValueError(f"First argument must be an integer greater than {min_value}. Got: {type(first_arg).__name__}: {first_arg}") from e
            
            return func(*args, **kwargs)
        
        return wrapper
    
    return decorator

if __name__ == '__main__':
    # Sample function to test the decorator
    def sample_function(a, b):
        """A simple function that adds two numbers."""
        return a + b

    @verify_first_argument(min_value=100)
    def failing_sample(x):
        """This will fail if x <= 100"""
        print(f"Processing {x}")
    
    # Test cases
    
    # Case 1: Valid input (greater than 100)
    try:
        result = sample_function(200, 50)
        print(f"Test 1 Passed: Result is {result}")
    except ValueError as e:
        print(f"Test 1 Failed with error: {e}")

    # Case 2: Invalid input (less than or equal to 100) - should raise ValueError
    try:
        result = failing_sample(50)
        print("Test 2 Unexpectedly succeeded")
    except ValueError as e:
        print(f"Test 2 Passed with expected error: {e}")

    # Case 3: Boundary case (equal to 100) - should raise ValueError because condition is strictly greater than (>), not >=
    try:
        result = failing_sample(100)
        print("Test 3 Unexpectedly succeeded")
    except ValueError as e:
        print(f"Test 3 Passed with expected error: {e}")

    # Case 4: Another valid input (just above 100)
    try:
        result = failing_sample(101)
        print("Test 4 Passed")
    except ValueError as e:
        print(f"Test 4 Failed with unexpected error: {e}")