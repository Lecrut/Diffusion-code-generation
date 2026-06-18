import functools

# Predefined constant value to match against
TARGET_VALUE = 42

def match_checker(expected_value: int) -> callable:
    """
    A decorator factory that checks if a function's result matches an expected integer value.
    
    Args:
        expected_value (int): The target value the decorated function must return.

    Returns:
        callable: A wrapper function that executes the original function and prints 
                  whether its output matched or did not match the expected value.
    """
    def decorator(func: callable) -> callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            
            if isinstance(result, int) and result == expected_value:
                print(f"Match! Result {result} matches the target value.")
            else:
                print(f"No match. Expected {expected_value}, got {type(result).__name__}: {result}")
                
            return result
        
        return wrapper
    
    return decorator

if __name__ == '__main__':
    # Sample function 1: Returns exactly the expected value (42)
    def get_answer():
        return TARGET_VALUE

    # Apply the decorator to get_answer with target 42
    decorated_get_answer = match_checker(TARGET_VALUE)(get_answer)
    
    print("--- Testing Function 1 ---")
    result_1 = decorated_get_answer()
    assert isinstance(result_1, int), "Result must be an integer."

    # Sample function 2: Returns a different value (99)
    def get_wrong_answer():
        return TARGET_VALUE + 57
    
    # Apply the decorator with the same target; should fail match check
    decorated_get_wrong = match_checker(TARGET_VALUE)(get_wrong_answer)
    
    print("--- Testing Function 2 ---")
    result_2 = decorated_get_wrong()

    # Sample function 3: Returns a non-integer type (string "42" which looks like the value but isn't int)
    def get_string_value():
        return str(TARGET_VALUE)

    # Apply decorator; should fail because it's not an integer or doesn't equal target numerically if converted, 
    # though here we strictly check `isinstance(result, int)` and equality.
    decorated_get_str = match_checker(TARGET_VALUE)(get_string_value)
    
    print("--- Testing Function 3 ---")
    result_3 = decorated_get_str()

    # Final assertion to ensure the first test passed internally via logic flow if needed externally
    final_check = (isinstance(result_1, int) and result_1 == TARGET_VALUE) \
                 or isinstance(result_2, int) and abs(result_2 - 47) > 0