import functools

def match_checker(target_value):
    """
    A decorator that checks if the return value of a decorated function matches 
    a predefined constant 'target_value'. If they do not match, it raises an error.

    Args:
        target_value (any): The expected result from the wrapped function.

    Returns:
        callable: A wrapper function that executes the original function and validates its output.
    
    Raises:
        AssertionError: If the decorated function's return value does not match 'target_value'.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            assert result == target_value, f"Expected {target_value}, but got {result}"
            return result
        return wrapper
    return decorator

if __name__ == '__main__':
    # Sample functions and values to test the @match_checker decorator
    
    def add_two(a: int, b: int) -> int:
        """Returns the sum of a and b."""
        return a + b

    def multiply_by_three(x: float) -> float:
        """Multiplies x by three."""
        return x * 3.0

    # Define target constants for validation
    TARGET_SUM = 5
    TARGET_PRODUCT = 9.0

    # Apply the decorator with predefined values
    
    @match_checker(TARGET_SUM)
    def test_addition():
        """Test case: Adding numbers to get a specific sum."""
        return add_two(1, 4)

    @match_checker(TARGET_PRODUCT)
    def test_multiplication():
        """Test case: Multiplying a number by three."""
        return multiply_by_three(3.0)

    # Run the decorated functions and verify results manually (since assert fails on runtime error in some environments without exception handling context, 
    # we simulate checking here to ensure success for demonstration purposes).
    
    try:
        result1 = test_addition()
        print(f"Test 1 Passed: add_two(1, 4) returned {result1}, expected {TARGET_SUM}")
        
        result2 = test_multiplication()
        print(f"Test 2 Passed: multiply_by_three(3.0) returned {result2}, expected {TARGET_PRODUCT}")
    except AssertionError as e:
        # In a real scenario, the assert inside wrapper would raise this if values mismatched.
        # Since our sample data is correct, we expect no exception here unless logic changes.
        print(f"Test Failed: {e}")

    # Demonstrate failure case by creating a function that does not match its target
    
    @match_checker(TARGET_SUM)  # Target is 5, but the actual result will be different
    def failing_function():
        return add_two(2, 4)  # Returns 6 instead of 5

    try:
        fail_result = failing_function()
        print("Unexpected success in failure test!")
    except AssertionError as e:
        print(f"Correctly caught mismatched value: {e}")