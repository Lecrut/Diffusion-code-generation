def compare_volumes(volume_a: float, volume_b: float) -> int:
    """
    Compares two numerical volumes to determine their relative magnitude.

    This function accepts any numeric input representing a volume quantity.
    It calculates the difference between the second volume and the first.
    
    Args:
        volume_a (float): The primary volume value for comparison. Can be positive, 
                          negative, or zero as it represents an abstract quantity here.
        volume_b (float): The secondary volume value to compare against the first.

    Returns:
        int: -1 if 'volume_a' is greater than 'volume_b', 
             0 if both values are equal, 
             +1 otherwise ('volume_a' < 'volume_b').

    Raises:
        TypeError: If either input argument is not a numeric type (int or float).
    
    Examples:
        >>> compare_volumes(5.0, 3.0)
        -1
        
        >>> compare_volumes(7.2, 7.2)
        0
        
        >>> compare_volumes(-2.0, -4.0)
        -1
    """
    
    # Validate input types to ensure only numeric values are processed
    if not isinstance(volume_a, (int, float)) or \
       not isinstance(volume_b, (int, float)):
        raise TypeError("Both arguments must be numbers.")

    difference = volume_b - volume_a
    
    return 1 if difference > 0 else (-1 if difference < 0 else 0)

if __name__ == '__main__':
    # Hard-coded sample values to test functionality without external input.
    SAMPLE_A: float = 42.5
    SAMPLE_B: float = 38.7

    result_code = compare_volumes(SAMPLE_A, SAMPLE_B)

    if result_code < 0:
        status_text = "Sample A is greater."
    elif result_code == 0:
        status_text = "Samples are equal."
    else:
        status_text = "Sample B is greater."

    print(f"Comparison Result for {SAMPLE_A} vs {SAMPLE_B}: {status_text}")