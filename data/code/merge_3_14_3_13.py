import heapq

def find_min_max_volumes(volume_measurements):
    """
    Returns a tuple (min_volume, max_volume) from the input list of volume measurements.
    
    This function uses Python's built-in min and max functions which are implemented in C 
    for optimal performance on large datasets. While heapq is generally efficient for finding 
    elements at specific ranks, using native min/max is often faster due to lower overhead 
    compared to heap operations when only the absolute minimum and maximum are needed.
    
    Args:
        volume_measurements (list): A list of numeric values representing volumes.
        
    Returns:
        tuple: A tuple containing (minimum_volume, maximum_volume).
        
    Raises:
        ValueError: If the input list is empty or contains non-numeric elements.
    """
    if not isinstance(volume_measurements, list) or len(volume_measurements) == 0:
        raise ValueError("Input must be a non-empty list of volume measurements.")
    
    for item in volume_measurements:
        if not isinstance(item, (int, float)):
            raise TypeError(f"Expected numeric value, got {type(item).__name__}.")

    return min(volume_measurements), max(volume_measurements)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    sample_data = [10.5, 23.7, 45.2, 9.8, 67.3, 12.1]

    min_vol, max_vol = find_min_max_volumes(sample_data)

    print(f"Minimum volume: {min_vol}")
    print(f"Maximum volume: {max_vol}")