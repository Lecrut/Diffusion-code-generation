import statistics as stats  # Only used if needed, but we'll implement manually below for clarity without imports unless necessary. Actually, let's just use built-in max/min which is C-optimized.

def find_min_max_volumes(volume_list):
    """
    Returns a tuple (min_volume, max_volume) from the input list of volumes.
    
    Args:
        volume_list (list[float]): A list containing numeric volume measurements.
        
    Returns:
        tuple[float]: The minimum and maximum values found in the list.
        
    Raises:
        ValueError: If the input list is empty or not provided.
    """
    if not isinstance(volume_list, list):
        raise TypeError("Input must be a list.")
    
    if len(volume_list) == 0:
        raise ValueError("The volume list cannot be empty.")

    # Using built-in max() and min() is highly efficient as they are implemented in C.
    return (min(volume_list), max(volume_list))

if __name__ == '__main__':
    # Hard-coded sample values representing large dataset simulation for testing efficiency
    sample_volumes = [10, 25, 30, 45, 67, 89, 12, 3.5, 99.9] * 1000
    
    min_vol, max_vol = find_min_max_volumes(sample_volumes)
    
    print(f"Minimum volume: {min_vol}")
    print(f"Maximum volume: {max_vol}")