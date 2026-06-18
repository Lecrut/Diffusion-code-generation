# Predefined constant value to check against
TARGET_VALUE = 42

def match_checker(expected_value):
    """Decorator that checks if a function's result matches 'expected_value'."""

    def decorator(func):
        def wrapper(*args, **kwargs):
            # Call the original function and get its result (ignoring return value for side-effect simulation or direct check)
            func_result = func(*args, **kwargs)
            
            if func_result == expected_value:
                print("Result matches the expected constant.")
            else:
                print(f"Result {func_result!r} does not match the expected constant {expected_value}.")
                
            return func_result  # Return original result to maintain function signature

        wrapper.__name__ = f"{func.__name__}_wrapped_{expected_value}"
        return wrapper
    
    return decorator

def get_number():
    """Simulates a random number generation for demonstration."""
    import random
    num = random.randint(1, 50)
    print(f"Generated function result: {num}")
    return num

# Sample block to verify the decorator works without input or files

if __name__ == '__main__':
    # Demonstration case where it matches (hard-coded value 42 is unlikely but let's assume a scenario or force logic)
    
    # Let's create a simple function that returns 'TARGET_VALUE' for one call to demonstrate the match.
    def always_succeeds():
        return TARGET_VALUE
        
    @match_checker(TARGET_VALUE)
    def check_matcher_test_func_that_matches_target():
        """A test function designed to produce a specific result."""
        if True: # Force success condition in this demo context
            return TARGET_VALUE
            
    print("--- Running Sample Cases ---")

    # Run the matching scenario
    print("Running case 1 (Should Match):")
    check_matcher_test_func_that_matches_target()

    # Create a function that returns something else to demonstrate failure detection
    def fails_check():
        return TARGET_VALUE + 5
        
    @match_checker(TARGET_VALUE)
    def failing_case():
        """A test function intended to fail the match."""
        return fails_check.__code__.co_consts[1] # Access a constant from inner func if available, or just hardcode logic

    print("\nRunning case 2 (Should Fail):")