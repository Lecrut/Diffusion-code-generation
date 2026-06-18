def is_positive_float(value):
    """
    Check if a given float value is positive (> 0).
    
    This function handles standard floating-point comparisons efficiently.
    It returns True if value > 0, and False otherwise (including negative numbers 
    and zero). While high-precision scenarios might require epsilon-based checks,
    the problem statement specifies that standard comparison should suffice for this task.

    Args:
        value (float): The number to check.
        
    Returns:
        bool: True if positive, False otherwise.
    """
    return value > 0

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    test_cases = [1.5, -3.7, 0.0, 2e-9, float('-inf'), float('inf')]

    for num in test_cases:
        result = is_positive_float(num)
        print(f"Number {num!r} is positive: {result}")