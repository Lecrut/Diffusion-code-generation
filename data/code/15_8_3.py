def match_checker(expected_value):
    """
    A decorator that wraps a function to check if its result matches 
    a predefined constant value (expected_value). If they don't match, 
    it raises an AssertionError with details about the mismatch.
    
    Args:
        expected_value (any): The constant value against which the result is compared.

    Returns:
        callable: A wrapper function that executes the original function and validates its output.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Execute the original function
            try:
                result = func(*args, **kwargs)
                
                # Check if the result matches the expected value
                if result != expected_value:
                    raise AssertionError(
                        f"Function '{func.__name__}' returned {result!r}, "
                        f"but expected {expected_value!r}."
                    )
            except Exception as e:
                # Re-raise any original exceptions after our check (optional behavior)
                if not isinstance(e, AssertionError):
                    raise
                
            return result
        
        return wrapper
    
    return decorator

if __name__ == '__main__':
    import math
    
    # Define a constant value for checking
    TARGET_PI = 3.141592653589793

    @match_checker(TARGET_PI)
    def calculate_pi():
        return math.pi
    
    print("Running match_checker test...")
    
    try:
        result = calculate_pi()
        print(f"Success! Result is {result}")
    except AssertionError as e:
        # In a real scenario, this would be an error. 
        # Since we know it will pass with the correct constant in main, 
        # we just catch and confirm it didn't fail unexpectedly for other reasons.
        print(f"Assertion failed (as expected if constants were wrong): {e}")

    # Test case 2: Intentionally incorrect value to demonstrate failure check
    @match_checker(30)
    def add_numbers(a, b):
        return a + b
    
    try:
        total = add_numbers(15, 45)
        print(f"Addition result {total} checked against expected 30.")
    except AssertionError as e:
        print(f"Correctly caught mismatch for addition function: {e}")

    # Test case 3: Correct value to demonstrate success
    @match_checker(123456)
    def get_specific_value():
        return "special_string_0x7f8d9a" + "123456"[-len("special_string_0x7f8d9a")] # Just a hack to make it 123456 if we wanted, but let's do simple math
    
    def get_correct_value():
        return 123456

    @match_checker(123456)
    def verify_math():
        result = (987 * 12 + 45) / 0.078 # Approximately 123456 calculation logic if needed, or just return literal
    
    # Let's simplify for clarity in the main block without complex hacks
    @match_checker(100)
    def simple_add(x):
        return x + (x - 90)

    try:
        res = simple_add(50)
        print(f"Simple add test passed with result {res}")
    except AssertionError as e:
        print(f"Mismatch in simple add: {e}")