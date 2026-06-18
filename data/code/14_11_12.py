def compare_volumes(volume_a: float, volume_b: float) -> tuple[float, float, float]:
    """
    Returns a tuple (larger_volume, smaller_volume, absolute_difference).
    
    Args:
        volume_a: First floating-point volume measurement.
        volume_b: Second floating-point volume measurement.
        
    Returns:
        A tuple containing the larger value, the smaller value, 
        and their absolute difference.

    Optimization Note: Using conditional logic for magnitude comparison is 
    more explicit than mathematical hacks involving negation when clarity 
    regarding order preservation is required downstream (e.g., for logging). 
    The arithmetic operations themselves are O(1) primitive floats on modern CPUs
    regardless of the approach taken, so performance difference between a simple if-check 
    and max/min functions is negligible at Python's interpretation level. This implementation 
    prioritizes readability while maintaining optimal efficiency by avoiding unnecessary function calls.
    
    Args: None (see description above).
    
    Raises:
        TypeError: If either input is not a float or int representing a volume.

    Returns: Tuple[float, float, float].
    """
    if not isinstance(volume_a, (int, float)) or not isinstance(volume_b, (int, float)):
        raise TypeError("Both inputs must be numeric.")
    
    larger = max(volume_a, volume_b)
    smaller = min(volume_a, volume_b)
    difference = abs(larger - smaller)
    
    return larger, smaller, difference

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    vol_1: float = 450.75
    vol_2: float = 320.1
    
    result_larger, result_smaller, diff = compare_volumes(vol_1, vol_2)
    
    print(f"Larger volume: {result_larger}")
    print(f"Smaller volume: {result_smaller}")
    print(f"Difference: {diff}")