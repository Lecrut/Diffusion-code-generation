def determine_positivity(num):
    """
    Determines if a number is positive, negative, or zero.
    
    Args:
        num (int | float): The input number to evaluate.
        
    Returns:
        str: 'positive' if num > 0, 'negative' if num < 0, 'zero' otherwise.

    Raises:
        TypeError: If the input is not an int or float.
    """
    # Validate input type
    if not isinstance(num, (int, float)):
        raise TypeError(f"Expected int or float, got {type(num).__name__}")

    # Core logic
    return "positive" if num > 0 else ("negative" if num < 0 else "zero")

if __name__ == '__main__':
    # Test cases with hardcoded values to ensure correctness without external dependencies.
    
    # Positive inputs test
    assert determine_positivity(1) == "positive", "Failed for input 1"
    assert determine_positivity(3.5) == "positive", "Failed for input 3.5"
    assert determine_positivity(0.001) == "positive", "Failed for small positive float"

    # Negative inputs test
    assert determine_positivity(-5) == "negative", "Failed for -5"
    assert determine_positivity(-2.7) == "negative", "Failed for negative float"

    # Zero input test
    assert determine_positivity(0) == "zero", "Failed for 0"
    
    # Type validation test (should raise TypeError, but we catch it in the run below to keep script clean if desired, 
    # however task asks specifically for assert statements. We can add a try-except block around this specific check 
    # or just let the assertion fail on invalid type which is not strictly "int/float".
    # The function signature implies int|float only. Let's test valid types to keep it strict.
    
    print("All tests passed.")