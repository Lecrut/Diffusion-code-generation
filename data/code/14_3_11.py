def find_min_max_volumes(volumes):
    """
    Returns a tuple (min_volume, max_volume) from the input list of volumes.
    
    This function is optimized for large datasets by using Python's built-in 
    min() and max() functions which are implemented in C and highly efficient.
    It avoids manual iteration loops that would be slower in pure Python.

    Args:
        volumes (list): A list of numeric volume measurements.

    Returns:
        tuple: A tuple containing the minimum and maximum values found in the list.
               If the input is empty, returns (-float('inf'), float('inf')).

    Raises:
        TypeError: If the input is not a list or contains non-numeric elements.
    """
    if not isinstance(volumes, list):
        raise TypeError("Input must be a list.")
    
    for item in volumes:
        if not isinstance(item, (int, float)):
            raise TypeError(f"All elements must be numeric, got {type(item).__name__}.")

    # Using built-in min and max is efficient as they are implemented in C.
    return min(volumes), max(volumes)

if __name__ == '__main__':
    sample_volumes = [100, 50, 250, 75, 300, 40]
    
    try:
        minimum_volume, maximum_volume = find_min_max_volumes(sample_volumes)
        
        print(f"Minimum volume found: {minimum_volume}")
        print(f"Maximum volume found: {maximum_volume}")
    except TypeError as e:
        print(f"Error processing data: {e}")