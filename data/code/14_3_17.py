def find_max_min_volumes(volumes):
    """
    Returns a tuple containing (max_volume, min_volume) from the input list.
    
    This function uses Python's built-in max() and min() functions which are implemented 
    in C for optimal performance on large datasets compared to manual iteration loops.
    
    Parameters:
        volumes (list of float or int): A non-empty list of volume measurements.
        
    Returns:
        tuple: (maximum_value, minimum_value) from the input list.
        
    Raises:
        ValueError: If the input list is empty.
    """
    if not volumes:
        raise ValueError("The volume list cannot be empty.")
    
    return max(volumes), min(volumes)

if __name__ == '__main__':
    # Hard-coded sample values representing volume measurements (liters).
    sample_volumes = [10.5, 23.4, 7.8, 99.2, 12.1, 45.6]

    max_vol, min_vol = find_max_min_volumes(sample_volumes)

    print(f"Maximum volume: {max_vol}")
    print(f"Minimum volume: {min_vol}")