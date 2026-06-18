def verify_first_argument(min_value: int = 100):
    """
    Decorator that verifies if the first argument passed to the wrapped function 
    is greater than or equal to a hardcoded constant (default 100).
    
    Args:
        min_value (int): The minimum threshold for the first argument. Default is 100.

    Returns:
        A decorator function that wraps another function and enforces the condition.
        
    Raises:
        ValueError: If the first argument is less than min_value.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            if args:
                first_arg = args[0]
                # Handle cases where first_arg might be a tuple (e.g., from list unpacking) or other types
                try:
                    numeric_first_arg = float(first_arg)
                except TypeError:
                    raise ValueError(f"First argument must be comparable to {min_value}, got type {type(first_arg).__name__}")

                if numeric_first_arg < min_value:
                    raise ValueError(
                        f"The first argument ({first_arg}) is not greater than or equal to the required value ({min_value})."
                    )
            return func(*args, **kwargs)
        wrapper.__name__ = func.__name__
        return wrapper
    return decorator

@verify_first_argument(min_value=100)
def process_data(value: int):
    """A sample function that processes data based on the first argument."""
    print(f"Processing value {value}")
    result = value * 2
    return result

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    
    # Test case 1: Valid input (greater than or equal to 100)
    try:
        output_valid = process_data(150)
        print(f"Success for valid input. Output: {output_valid}")
    except ValueError as e:
        print(f"Error with valid input: {e}")

    # Test case 2: Invalid input (less than 100)
    try:
        output_invalid = process_data(50)
        print("This should not be reached.")
    except ValueError as e:
        print(f"Expected error for invalid input: {e}")

    # Test case 3: Boundary value (exactly 100) - Should pass
    try:
        output_boundary = process_data(100)
        print(f"Success for boundary input. Output: {output_boundary}")
    except ValueError as e:
        print(f"Unexpected error with boundary input: {e}")

    # Test case 4: Negative number - Should fail
    try:
        output_negative = process_data(-10)
        print("This should not be reached.")
    except ValueError as e:
        print(f"Expected error for negative input: {e}")