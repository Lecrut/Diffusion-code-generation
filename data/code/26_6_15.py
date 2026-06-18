import functools

# Hardcoded constant for comparison
CONSTANT = 100

def validate_first_arg_greater_than_constant(func):
    """Decorator that checks if the first argument is greater than CONSTANT."""
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Access the first positional argument from args tuple
        first_argument = args[0] if args else None
        
        if not isinstance(first_argument, (int, float)):
            raise ValueError("First argument must be a number.")
        
        if not (first_argument > CONSTANT):
            raise ValueError(
                f"The first argument ({first_argument}) is not greater than {CONSTANT}."
            )
        
        return func(*args, **kwargs)
    
    return wrapper

if __name__ == '__main__':
    # Sample function to wrap for testing
    @validate_first_arg_greater_than_constant
    def process_data(value):
        """Sample function that expects a number greater than 100."""
        print(f"Processing data with value: {value}")

    # Test case 1: Valid input (greater than CONSTANT)
    try:
        result = process_data(250)
        print("Test 1 passed.")
    except ValueError as e:
        print(f"Unexpected error in Test 1: {e}")

    # Test case 2: Invalid input (not greater than CONSTANT)
    try:
        result = process_data(90)
        print("Test 2 failed - should have raised an exception.")
    except ValueError as e:
        print(f"Expected error in Test 2 received correctly.")

    # Test case 3: Boundary condition (equal to CONSTANT, not greater)
    try:
        result = process_data(100.5)
        print("Test 3 failed - should have raised an exception.")
    except ValueError as e:
        print(f"Expected error in Test 3 received correctly.")

    # Additional test with tuple unpacking simulation (if needed for edge cases, though args are simple here)
    @validate_first_arg_greater_than_constant
    def helper(data):
        return data * 2
    
    try:
        out = helper(150)
        print(f"Helper output correct: {out}")
    except Exception as e:
        print(f"Unexpected error in Helper test: {e}")