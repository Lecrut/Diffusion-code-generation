import functools

# Predefined constant value to match against
TARGET_VALUE = 42

def match_checker(target_value: int) -> callable:
    """
    A decorator that checks if the result of a function matches a predefined target value.
    
    Args:
        target_value (int): The expected return value from the decorated function.
        
    Returns:
        callable: A wrapper function that executes the original function and verifies its output.
                  If the output does not match, it raises an AssertionError with details.
    """

    def decorator(func: callable) -> callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            
            # Check if the result matches the target value
            assert isinstance(result, int), f"Expected integer but got {type(result).__name__}"
            assert result == target_value, (
                f"Function '{func.__name__}' returned {result}, "
                f"but expected to match constant: {target_value}"
            )
            
            return result
        
        return wrapper

    return decorator

if __name__ == '__main__':
    # Sample function that should pass the check (returns 42)
    def correct_function():
        return TARGET_VALUE
    
    # Apply the decorator with our predefined constant
    decorated_correct = match_checker(TARGET_VALUE)(correct_function)
    
    try:
        result = decorated_correct()
        print(f"Correct function executed successfully. Result: {result}")
    except AssertionError as e:
        print(f"AssertionError in correct_function (unexpected): {e}")

    # Sample function that should fail the check (returns 10)
    def incorrect_function():
        return 10
    
    decorated_incorrect = match_checker(TARGET_VALUE)(incorrect_function)
    
    try:
        result = decorated_incorrect()
        print(f"Incorrect function executed successfully. Result: {result}")
    except AssertionError as e:
        print(f"AssertionError in incorrect_function (expected): {e}")

    # Sample function that returns a non-integer to test type checking
    def wrong_type_function():
        return "string_result"
    
    decorated_wrong_type = match_checker(TARGET_VALUE)(wrong_type_function)
    
    try:
        result = decorated_wrong_type()
        print(f"Wrong type function executed successfully. Result: {result}")
    except AssertionError as e:
        print(f"AssertionError in wrong_type_function (expected): {e}")

    # Demonstrate using the decorator with a different target value for variety
    def another_correct_func():
        return 100
    
    decorated_another = match_checker(100)(another_correct_func)
    
    try:
        result = decorated_another()
        print(f"Another correct function executed successfully. Result: {result}")
    except AssertionError as e:
        print(f"AssertionError in another_correct_func (unexpected): {e}")

    # Demonstrate failure with a different target value mismatch
    def wrong_target_function():
        return 100
    
    decorated_wrong_target = match_checker(42)(wrong_target_function)
    
    try:
        result = decorated_wrong_target()
        print(f"Wrong target function executed successfully. Result: {result}")
    except AssertionError as e:
        print(f"AssertionError in wrong_target_function (expected): {e}")

    # Summary of execution status
    print("\n--- Execution Status ---")
    print("1. Correct value match: PASSED")
    print("2. Incorrect integer value: FAILED (as expected)")
    print("3. Non-integer return type: FAILED (type check + value mismatch)")
    print("4. Different correct target: PASSED")
    print("5. Mismatched different targets: FAILED (as expected)")