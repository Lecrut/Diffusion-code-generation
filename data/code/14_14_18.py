def compare_volumes(volume_a: float, volume_b: float) -> dict:
    """
    Compares two volume measurements and returns a dictionary with 
    original values, calculated ratio (larger/smaller), and equality status.
    
    Args:
        volume_a (float): First volume measurement.
        volume_b (float): Second volume measurement.
        
    Returns:
        dict: A dictionary containing 'volumes', 'ratio', and 'are_equal'.
              - volumes: List of [volume_a, volume_b]
              - ratio: Float representing larger/smaller (1.0 if equal)
              - are_equal: Boolean indicating if both values match exactly
    """
    # Determine which is the smaller value to avoid division by zero logic errors
    min_val = min(volume_a, volume_b)
    
    # Calculate ratio; handle potential floating point edge cases gracefully
    if min_val == 0.0:
        raise ValueError("Cannot calculate ratio when one or both volumes are zero.")
        
    larger_val = max(volume_a, volume_b)
    calculated_ratio = larger_val / min_val
    
    return {
        "volumes": [volume_a, volume_b],
        "ratio": calculated_ratio,
        "are_equal": (volume_a == volume_b)
    }

if __name__ == "__main__":
    # Hard-coded sample values for testing without user input or external dependencies
    vol_1 = 50.0
    vol_2 = 75.0
    
    result = compare_volumes(vol_1, vol_2)
    
    print(f"Volumes: {result['volumes']}")
    print(f"Ratio (larger/smaller): {result['ratio']:.4f}")
    print(f"Are equal? {result['are_equal']}")