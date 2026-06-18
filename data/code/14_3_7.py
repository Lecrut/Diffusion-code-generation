import statistics as stats

def find_min_max_volumes(volume_list):
    """
    Returns a tuple (min_volume, max_volume) from the input list of volumes.
    
    This function uses built-in optimized methods to ensure high efficiency 
    for large datasets by avoiding manual iteration loops in Python bytecode.

    Parameters:
        volume_list (list[float]): A list containing numeric volume measurements.

    Returns:
        tuple[float, float]: The minimum and maximum values found in the list.

    Raises:
        TypeError: If input is not a list or contains non-numeric elements.
        ValueError: If the input list is empty.
    """
    
    if not isinstance(volume_list, list):
        raise TypeError("Input must be a list.")
        
    for item in volume_list:
        try:
            float(item)
        except (TypeError, ValueError):
            raise TypeError(f"List contains non-numeric value: {item}")

    if len(volume_list) == 0:
        raise ValueError("The input list is empty; cannot determine min or max.")

    
    return min(volume_list), max(volume_list)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction
    sample_volumes = [15.2, 30.7, 45.9, 10.1, 60.3]

    min_vol, max_vol = find_min_max_volumes(sample_volumes)

    print(f"Minimum volume: {min_vol}")
    print(f"Maximum volume: {max_vol}")