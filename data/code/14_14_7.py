def compare_volumes(volume_a: float, volume_b: float) -> dict:
    """
    Compares two volume measurements and returns a dictionary with 
    original volumes, their ratio (larger/smaller), and equality status.
    
    Args:
        volume_a (float): First volume measurement.
        volume_b (float): Second volume measurement.
        
    Returns:
        dict: A dictionary containing 'volumes', 'ratio', and 'is_equal'.
              Raises ValueError if both volumes are zero or negative logic fails, 
              though typically ratio is undefined for equal zeros; handled gracefully here.
    """
    # Determine which is larger to calculate the correct ratio direction
    max_vol = max(volume_a, volume_b)
    min_vol = min(volume_a, volume_b)

    if min_vol == 0:
        raise ValueError("Cannot compute a meaningful ratio when one or both volumes are zero.")

    calculated_ratio = max_vol / min_vol
    
    return {
        "volumes": [volume_a, volume_b],
        "ratio": calculated_ratio,
        "is_equal": (volume_a == volume_b)
    }

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    vol_1 = 50.0
    vol_2 = 75.0
    
    result = compare_volumes(vol_1, vol_2)
    
    print(f"Volumes: {result['volumes']}")
    print(f"Ratio (larger/smaller): {result['ratio']:.4f}")
    print(f"Are volumes equal? {result['is_equal']}")