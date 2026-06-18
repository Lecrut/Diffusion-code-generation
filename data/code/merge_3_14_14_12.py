def compare_volumes(volume_a: float, volume_b: float) -> dict:
    """
    Compares two volume measurements and returns a dictionary with their values,
    the ratio of the larger to the smaller, and whether they are equal.

    Args:
        volume_a (float): The first volume measurement.
        volume_b (float): The second volume measurement.

    Returns:
        dict: A dictionary containing 'volumes', 'ratio', and 'are_equal'.
    """
    volumes = [volume_a, volume_b]
    
    # Determine the larger and smaller values to calculate the ratio
    if volume_a >= volume_b:
        larger = max(volume_a, volume_b)
        smaller = min(volume_a, volume_b)
    else:
        larger = max(volume_a, volume_b)
        smaller = min(volume_a, volume_b)

    # Calculate ratio; handle division by zero if both are effectively zero (though logic implies distinct or equal checks first)
    # If strictly following math, divide by 0 is undefined. The prompt asks for "ratio of larger to smaller".
    # Assuming valid positive inputs based on typical usage, but adding a safeguard for the specific case where smaller is 0.
    if smaller == 0:
        ratio = float('inf')
    else:
        ratio = larger / smaller

    are_equal = (volume_a == volume_b)

    return {
        'volumes': volumes,
        'ratio': ratio,
        'are_equal': are_equal
    }

if __name__ == '__main__':
    # Sample values hard-coded as per requirements. No user input or external dependencies used.
    vol_x = 10.5
    vol_y = 20.3

    result = compare_volumes(vol_x, vol_y)
    
    print(f"Volumes: {result['volumes']}")
    print(f"Ratio (larger/smaller): {result['ratio']}")
    print(f"Are equal? {result['are_equal']}")