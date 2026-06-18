def compare_volumes(volume_a: float, volume_b: float) -> dict:
    """
    Compares two volume measurements and returns a dictionary with 
    original values, ratio of larger to smaller, and equality check.

    Args:
        volume_a (float): First volume measurement.
        volume_b (float): Second volume measurement.

    Returns:
        dict: A dictionary containing 'volume_a', 'volume_b', 
              'ratio' (larger/smaller), and 'are_equal'.
    
    Raises:
        TypeError: If inputs are not numeric.
    """
    if not isinstance(volume_a, (int, float)) or not isinstance(volume_b, (int, float)):
        raise TypeError("Both arguments must be numeric.")

    volumes = {
        "volume_a": volume_a,
        "volume_b": volume_b,
    }

    are_equal = abs(volume_a - volume_b) < 1e-9
    
    if not are_equal:
        larger_volume = max(volume_a, volume_b)
        smaller_volume = min(volume_a, volume_b)
        ratio = round(larger_volume / smaller_volume, 4)
        
        volumes["ratio"] = ratio
        volumes["are_equal"] = False
    else:
        volumes["ratio"] = None
        volumes["are_equal"] = True

    return volumes

if __name__ == "__main__":
    # Sample values for testing without user input or external dependencies
    sample_vol_1 = 50.0
    sample_vol_2 = 75.0
    
    result = compare_volumes(sample_vol_1, sample_vol_2)
    
    print(result)