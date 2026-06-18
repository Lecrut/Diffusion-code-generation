import functools

def check_first_arg(condition_value=100):
    """
    Decorator that verifies if the first argument is greater than condition_value (default 100).
    
    Args:
        condition_value: The constant threshold to compare against. Defaults to 100.

    Returns:
        A decorator function that wraps another function and checks the first argument on execution.
        
    Raises:
        ValueError: If the first argument is not greater than condition_value.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if args[0] <= condition_value:
                raise ValueError(f"The first argument ({args[0]}) must be greater than {condition_value}.")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@check_first_arg(100)
def example_function(x):
    """A sample function that performs a simple operation based on the first argument."""
    print(f"Processing value: {x}")
    return x * 2

if __name__ == '__main__':
    # Test case where condition is met (value > 100)
    try:
        result = example_function(500)
        print(f"Success! Result: {result}")
    except ValueError as e:
        print(f"Validation error caught: {e}")

    # Test cases where condition is not met (values <= 100), expected to raise errors
    test_values = [10, 50, 99]
    for val in test_values:
        try:
            result = example_function(val)
            print(f"Unexpected success with value {val}: {result}")
        except ValueError as e:
            print(f"Expected error caught for value {val}: {e}")

    # Another call to verify the working case again
    try:
        result = example_function(200)
        print(f"Second successful execution Result: {result}")
    except ValueError as e:
        print(f"Unexpected validation failure: {e}")