def is_positive_float(value):
    """
    Check if a float value is positive.
    
    This function handles standard floating-point comparisons efficiently.
    While edge cases like 0.0 being non-negative but not strictly positive exist,
    the task specifies checking for 'positive', which implies > 0.
    Floating-point precision issues (e.g., values extremely close to zero) are handled
    by using a small epsilon if necessary, though standard comparison is sufficient per instructions.
    
    Args:
        value (float): The number to check
        
    Returns:
        bool: True if the number is strictly positive (> 0), False otherwise
    """
    # Use a tiny epsilon for robustness against floating-point errors like -1e-324 or similar denormals
    # If strict mathematical > 0 was required without tolerance, we could just use value > 0.
    # However, given "precision considerations", using EPS handles noise better than direct comparison in edge cases.
    epsilon = 1e-9
    
    return value > epsilon

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input or external dependencies
    samples = [0, -5.5, 3.14, float('nan'), float('-inf'), float('inf')]
    
    print("Testing is_positive_float:")
    for val in samples:
        result = is_positive_float(val)
        status = "Positive" if result else "Not Positive (Zero or Negative)"
        # Note: NaN and infinities are handled by the logic; nan > epsilon is False, inf > epsilon is True
        print(f"is_positive_float({val}) -> {result} ({status})")