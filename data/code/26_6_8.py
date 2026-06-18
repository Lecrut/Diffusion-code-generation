def verify_first_argument(condition_value: int = 100):
    """
    A decorator factory that verifies if the first argument passed to a function 
    is greater than a hardcoded constant (default 100). If not, it raises ValueError.
    
    Args:
        condition_value (int): The threshold value for comparison. Default is 100.
        
    Returns:
        Decorator function that enforces the argument check before executing the wrapped function.
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            if args and not isinstance(args[0], (int, float)):
                raise ValueError("The first argument must be a number.")
            
            try:
                value = int(args[0]) if len(args) > 1 else args[0]
            except (ValueError, TypeError):
                raise ValueError(f"First argument '{args[0]}' is not convertible to an integer or float.")

            if value <= condition_value:
                raise ValueError(
                    f"The first argument ({value}) must be greater than {condition_value}."
                )
            
            return func(*args, **kwargs)
        return wrapper
    
    return decorator

@verify_first_argument()
def process_data(data):
    """A sample function that processes data after the verification."""
    print(f"Processing data: {data}")
    # Simulate some processing logic
    result = f"Result for {data}"
    return result

if __name__ == '__main__':
    try:
        # Test case 1: Valid input (greater than 100)
        print("Running valid test...")
        output = process_data(250)
        print(f"Output from valid test: {output}\n")

        # Test case 2: Invalid input (less than or equal to 100) - should raise ValueError
        print("Testing invalid input condition...")
        try:
            output = process_data(85)
        except ValueError as e:
            print(f"Expected error caught for value <= 100: {e}\n")

    except Exception as e:
        # Fallback in case of unexpected errors during execution flow unrelated to the decorator logic
        print(f"An unexpected error occurred: {type(e).__name__}: {e}")