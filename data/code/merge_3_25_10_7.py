def is_zero(value):
    """
    Returns True if value is exactly zero, False otherwise.
    
    Args:
        value (numeric): A single numerical argument.
        
    Returns:
        bool: True if value equals 0.0 or equivalent integer, else False.
    """
    return value == 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without external input
    test_values = [0, 1, -1, 0.0, -0.0, float('inf'), -float('inf')]
    
    results = []
    for val in test_values:
        result = is_zero(val)
        results.append(result)
    
    # Output results to standard output (no interactive input required)
    print(results)