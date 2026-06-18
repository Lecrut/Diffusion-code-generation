class NegativeResultError(Exception):
    """Custom exception raised when a function returns a negative value."""
    pass

def check_non_negative(func):
    """Decorator that checks if the result of func is non-negative.
    
    If the result is negative, raises NegativeResultError with the 
    original return value and arguments as context.
    
    Args:
        func (callable): The function to decorate.
        
    Returns:
        callable: The wrapped decorator-enhanced function.
    """
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            
            # Handle cases where the original return value is not a number
            if isinstance(result, (int, float)):
                if result < 0:
                    raise NegativeResultError(
                        f"Function {func.__name__} returned a negative value ({result}).",
                        func=func,
                        args=args,
                        kwargs=kwargs
                    )
                
            return result
            
        except Exception as e:
            # Re-raise any exceptions that were already raised by the function
            raise
    
    return wrapper

@check_non_negative
def calculate_distance(x1, y1, x2, y2):
    """Calculates Euclidean distance between two points.
    
    Args:
        x1 (float): X-coordinate of point 1.
        y1 (float): Y-coordinate of point 1.
        x2 (float): X-coordinate of point 2.
        y2 (float): Y-coordinate of point 2.
        
    Returns:
        float: The distance between the two points.
    """
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

@check_non_negative
def calculate_area(radius):
    """Calculates area of a circle using radius squared to simulate potential negative input test case.
    
    Note: In reality, math.pi * r^2 is always non-negative for real numbers.
    This function is designed specifically to allow testing the decorator with 
    invalid inputs that might result in unexpected behavior if logic were different.
    """
    # Simulating a scenario where we want to test negative handling explicitly
    # by returning -1 directly when radius < 0 (though mathematically area can't be negative)
    return abs(radius ** 2 * 3.14159) if radius >= 0 else -radius

if __name__ == '__main__':
    # Test Case 1: Valid positive result for calculate_distance
    try:
        dist = calculate_distance(0, 0, 3, 4)
        print(f"Distance calculated successfully: {dist}")
    except NegativeResultError as e:
        print(f"Negative Result Error in distance calculation (unexpected): {e.args[1]}")

    # Test Case 2: Valid positive result for calculate_area
    try:
        area = calculate_area(5)
        print(f"Area calculated successfully: {area}")
    except NegativeResultError as e:
        print(f"Negative Result Error in area calculation (unexpected): {e.args[1]}")

    # Test Case 3: Simulating a negative return scenario for testing the decorator logic directly.
    # Since calculate_area uses abs, we create a helper to test strict negativity check if needed later,
    # but here we demonstrate that normal usage is fine and show how an error would look 
    # by manually triggering it or using a function known to fail (though none provided in this snippet).
    
    # To strictly satisfy the requirement of testing negative handling without changing existing logic:
    # We will define a simple test helper inside main to demonstrate failure case clearly.
    def failing_function():
        return -5
    
    try:
        result = check_non_negative(failing_function)()
        print("Unexpected success")
    except NegativeResultError as e:
        print(f"Caught expected error for negative value (-5): {e}")

    # Test Case 4: Attempting to use a hypothetical function that returns -10 
    # (simulated by calling the failing helper again)
    try:
        result = check_non_negative(failing_function)()
    except NegativeResultError as e:
        print(f"Caught expected error for negative value (-5): {e}")

    print("All tests completed.")