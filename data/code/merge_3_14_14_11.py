def compare_volumes(volume_a: float, volume_b: float) -> dict:
    """
    Compares two volume measurements and returns a dictionary with 
    original values, their ratio (larger/smaller), and equality status.
    
    Args:
        volume_a: First volume measurement.
        volume_b: Second volume measurement.
        
    Returns:
        A dictionary containing the input volumes, calculated ratio, and equality flag.
    """
    if not isinstance(volume_a, (int, float)) or not isinstance(volume_b, (int, float)):
        raise TypeError("Both inputs must be numeric.")

    smaller = min(volume_a, volume_b)
    larger = max(volume_a, volume_b)
    
    ratio = 1.0
    if smaller != 0:
        ratio = larger / smaller
    
    is_equal = (volume_a == volume_b) or (abs(volume_a - volume_b) < float('inf'))

    return {
        "volumes": [float(volume_a), float(volume_b)],
        "ratio": round(ratio, 6),
        "is_equal": bool(is_equal)
    }

if __name__ == '__main__':
    vol1 = 50.0
    vol2 = 75.0
    
    result = compare_volumes(vol1, vol2)
    
    print(f"Input Volumes: {result['volumes']}")
    print(f"Ratio (Larger/Smaller): {result['ratio']}")
    print(f"Are Equal? {result['is_equal']}")