def verify_argument(value):
    """Decorator factory that verifies if an argument is greater than a constant."""
    
    def decorator(func):
        # Hardcoded constant as per requirement
        CONSTANT = 100
        
        def wrapper(*args, **kwargs):
            first_arg = args[0] if args else None
            
            try:
                numeric_value = float(first_arg)
                
                if not (numeric_value > CONSTANT):
                    raise ValueError(f"First argument {first_arg} must be greater than the constant 100.")
                    
            except TypeError as e:
                # Handle cases where first arg is not a number or cannot be converted to float
                raise ValueError(f"First argument must be numeric and greater than 100. Got type of '{type(first_arg).__name__}'.") from None
                
            return func(*args, **kwargs)
        
        wrapper.__name__ = f"{func.__name__}.wrapped"
        return wrapper
    
    return decorator

@verify_argument(100)
def process_data(data):
    """Sample function to be decorated."""
    print(f"Processing data: {data}")
    return data * 2

if __name__ == '__main__':
    # Test case 1: Valid input (greater than 100)
    try:
        result = process_data(200)
        print("Success:", result)
    except ValueError as e:
        print(f"Error in valid test: {e}")

    # Test case 2: Invalid input (less than or equal to 100)
    try:
        result = process_data(50)
        print("Unexpected success with invalid input:", result)
    except ValueError as e:
        print(f"Expected error for invalid test: {e}")

    # Test case 3: Invalid type (string instead of number)
    try:
        result = process_data("invalid")
        print("Unexpected success with string input:", result)
    except ValueError as e:
        print(f"Expected error for non-numeric input: {e}")