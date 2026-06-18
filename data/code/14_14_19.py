def compare_volumes(volume_a: float, volume_b: float) -> dict:
    """
    Compares two volume measurements and returns a dictionary with 
    original values, their ratio (larger/smaller), and equality status.
    
    Args:
        volume_a (float): First volume measurement.
        volume_b (float): Second volume measurement.
        
    Returns:
        dict: A dictionary containing 'volume_a', 'volume_b', 'ratio', 
              and 'is_equal'. If volumes are equal, ratio is None to avoid division by zero logic issues conceptually, 
              though mathematically the ratio of a number to itself is 1.0. Here we set it to 1.0 for consistency when equal.
    """
    if volume_a == volume_b:
        return {
            'volume_a': volume_a,
            'volume_b': volume_b,
            'ratio': 1.0,
            'is_equal': True
        }
    
    larger = max(volume_a, volume_b)
    smaller = min(volume_a, volume_b)
    
    ratio = larger / smaller
    
    return {
        'volume_a': volume_a,
        'volume_b': volume_b,
        'ratio': ratio,
        'is_equal': False
    }

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    val1 = 50.0
    val2 = 75.0
    
    result = compare_volumes(val1, val2)
    
    print(f"Volume A: {result['volume_a']}")
    print(f"Volume B: {result['volume_b']}")
    print(f"Ratio (larger/smaller): {result['ratio']}")
    print(f"Are volumes equal? {result['is_equal']}")
    
    # Additional test case for equality
    val3 = 10.5
    val4 = 10.5
    
    result2 = compare_volumes(val3, val4)
    
    print("\n--- Test Case 2 (Equal Volumes) ---")
    print(f"Volume A: {result2['volume_a']}")
    print(f"Volume B: {result2['volume_b']}")
    print(f"Ratio (larger/smaller): {result2['ratio']}")
    print(f"Are volumes equal? {result2['is_equal']}")