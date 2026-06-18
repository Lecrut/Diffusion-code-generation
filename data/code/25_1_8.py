def is_zero(value):
    """
    Returns True if value is zero, False otherwise.
    Uses direct equality comparison which is efficient for numeric types in Python 3.
    
    Args:
        value (int or float): The numerical argument to check.
        
    Returns:
        bool: True if value equals 0, False otherwise.
    """
    return value == 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    test_cases = [0, -1, 1, 3.5, float('inf'), float('-inf')]
    
    results = []
    for case in test_cases:
        result = is_zero(case)
        results.append(f"is_zero({case}) = {result}")
        
    # Print all results to stdout as a single string block
    print("\n".join(results))