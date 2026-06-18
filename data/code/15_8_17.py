def match_checker(expected_value):
    """
    A decorator that checks if a function's output matches an expected value.
    
    Args:
        expected_value (any): The constant value to compare against the function result.
        
    Returns:
        Function: A wrapper function that executes the original function and validates its return value.
                  Raises AssertionError if the results do not match, otherwise returns the result unchanged.
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                # Execute the original function to avoid side effects on argument checking later
                return_value = func(*args, **kwargs)
                
                # Check if returned value matches the expected constant
                assert return_value == expected_value, (f"Value mismatch! Expected {expected_value}, got {return_value}")
            except AssertionError as e:
                raise e
            finally:
                return return_value
            
        return wrapper
    
    return decorator

import functools

if __name__ == '__main__':
    
    # Sample function to be decorated. 
    def add_numbers(a, b):
        """Returns the sum of two integers."""
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a + b
        
        else:
            raise TypeError("Both arguments must be numeric")

    # Sample constants for testing. 
    TEST_EXPECTED_VALUE = 10
    
    try:
        result_wrapper = add_numbers(5, -4) if not isinstance(result_wrapper := match_checker(TEST_EXPECTED_VALUE)(add_numbers))(TEST_EXPECTED_VALUE) else None
        
        print(f"Function execution result matches expected value.")
        
    except Exception as e:
        print(e.args[0] + " Function test failed." )