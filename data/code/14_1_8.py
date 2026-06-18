def compare_volumes(volume_a: float, volume_b: float) -> str:
    """
    Compares two volume measurements and returns a descriptive string.
    
    Parameters:
        volume_a (float): First volume measurement.
        volume_b (float): Second volume measurement.
        
    Returns:
        str: Description of the relationship between the volumes.
    """
    if abs(volume_a - volume_b) < 1e-9:
        return f"Volume A ({volume_a}) is equal to Volume B ({volume_b})."
    
    if volume_a > volume_b:
        return f"Volume A ({volume_a}) is larger than Volume B ({volume_b})."
    
    return f"Volume A ({volume_a}) is smaller than Volume B ({volume_b})."

if __name__ == '__main__':
    # Hard-coded sample values for testing without any user input.
    result = compare_volumes(10.5, 7.2)
    print(result)
    
    test_cases = [
        (3.4, 3.4),      # Equal case with standard float representation
        (-5.0, -8.9),   # Negative numbers where A is larger
        (1e-6, 0),       # Very small positive vs zero
    ]
    
    print("--- Additional Test Cases ---")
    for a, b in test_cases:
        res = compare_volumes(a, b)
        print(f"Comparing {a} and {b}: {res}")