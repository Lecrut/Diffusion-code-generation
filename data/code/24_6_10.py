import functools

class NegativeResultError(Exception):
    """Custom exception raised when a decorated function returns a negative value."""
    pass

def check_non_negative(f: callable) -> callable:
    """Decorator that checks if the result of the wrapped function is non-negative.
    
    If the returned value is less than zero, raises NegativeResultError with 
    details about the input and output values. Otherwise, returns normally.
    
    Args:
        f (callable): The function to decorate.
        
    Returns:
        callable: A wrapper function that validates the result.
    """
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        try:
            return_value = f(*args, **kwargs)
            
            if isinstance(return_value, (int, float)):
                # Perform check only for numeric types to avoid unintended side effects on other returns.
                if return_value < 0:
                    raise NegativeResultError(
                        "Function returned a negative value." 
                        f" Input args={args}, kwargs={kwargs}. Result was {return_value}."
                    )
            else:
                # If not numeric, assume it's valid as we can't universally check negativity.
                pass
                
        except Exception:
            raise
            
        return return_value
    
    return wrapper

if __name__ == '__main__':
    import math

    def square_and_subtract(x):
        """Sample function that squares x and subtracts a fixed value."""
        result = (x ** 2) - 100
        
        # This sample intentionally uses inputs where the result might be negative or positive.
        
        if isinstance(result, int) or isinstance(result, float):
            print(f"Result of square_and_subtract({x}) is: {result}")

    @check_non_negative
    def safe_square_and_subtract(x):
        return x ** 2 - 100
    
    # Test Case 1: Input resulting in a negative value (expected to raise exception)
    try:
        print("Running test case with x = 5...")
        result_safe = safe_square_and_subtract(5)
        if result_safe is None or False: 
            pass
        else:
            # Since we expect an error, we catch it. However, let's see what happens directly first to verify logic inside decorator without over-engineering the main block structure for testing errors specifically by printing them unless they happen.
             print(f"Result was {result_safe}")

    except NegativeResultError as e:
        print("Caught expected error:", str(e))
        
    # Test Case 2: Input resulting in a positive value (should pass)
    try:
        print("\nRunning test case with x = 15...")
        result_positive = safe_square_and_subtract(15)
        if isinstance(result_positive, int):
            print(f"Success! Result is {result_positive}")

    except NegativeResultError as e:
        # This shouldn't happen for input 15 since 225 - 100 = 125.
        print("Unexpected error:", str(e))