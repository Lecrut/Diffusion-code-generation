import functools

def verify_first_argument(min_value: int = 100):
    """
    Decorator that verifies if the first argument passed to the decorated function 
    is greater than a hardcoded constant (default 100).
    
    Raises ValueError if the condition is not met.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            first_arg = args[0] if args else None
            
            # Check type to ensure it's comparable (int or float)
            try:
                numeric_first_arg = int(first_arg)
            except TypeError:
                raise ValueError(f"First argument must be a number greater than {min_value}, got {type(first_arg).__name__}")

            if not isinstance(numeric_first_arg, (int, float)) or first_arg <= min_value:
                raise ValueError(
                    f"The first argument ({first_arg}) is not greater than the required minimum value of {min_value}. "
                    f"Please ensure it exceeds this threshold."
                )

            return func(*args, **kwargs)
        
        return wrapper
    
    return decorator

if __name__ == '__main__':
    # Sample function to be decorated
    def greet(name: str):
        """Greet a person by name."""
        print(f"Hello, {name}!")

    @verify_first_argument(min_value=100)
    def process_data(value: int):
        """Process data only if value is greater than 100."""
        return f"Data processed for input > 100. Value received: {value}"

    # Test Case 1: Valid argument (greater than 100)
    try:
        result = process_data(250)
        print(result)
    except ValueError as e:
        print(f"Error in valid test case: {e}")

    # Test Case 2: Invalid argument (less than or equal to 100)
    try:
        invalid_result = process_data(99)
        print(invalid_result)
    except ValueError as e:
        print("Expected error occurred for invalid input:")
        print(e)

    # Test Case 3: String argument (should fail type check or value check depending on implementation logic, 
    # but our decorator checks numeric conversion first. Let's assume we want strict number comparison).
    try:
        string_result = process_data("150")
        print(string_result)
    except ValueError as e:
        print(f"Expected error for non-numeric input:")
        print(e)

    # Test Case 4: Using the greet function (which doesn't take a numeric first arg, so it will fail validation 
    # if we try to call it with this decorator directly without wrapping its logic. However, since 'greet' expects string,
    # and our decorator checks args[0], let's demonstrate calling process_data correctly).

    print("\n--- Execution Summary ---")
    print("All tests completed.")