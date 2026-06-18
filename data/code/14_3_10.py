import statistics as stats  # Note: 'statistics' is a standard library module; we use it here if needed, but logic is manual below to avoid overhead unless specified otherwise. However, since no specific external libraries are requested and built-in functions are preferred for efficiency without imports where possible (except stdlib), let's stick to pure Python or minimal stdlib usage. Actually, min/max on lists in CPython are highly optimized built-ins.

def find_volume_extremes(volumes):
    """
    Returns a tuple containing the maximum and minimum volume from the input list.
    
    Args:
        volumes (list[float]): A list of numerical values representing volume measurements.
        
    Returns:
        tuple[float, float]: A tuple where the first element is the max value 
                            and the second is the min value found in 'volumes'.
                            
    Raises:
        ValueError: If the input list is empty or does not contain only numeric types.
    """
    if not volumes:
        raise ValueError("Input list cannot be empty.")
    
    # Check that all elements are numbers (int, float) to avoid TypeError later
    for item in volumes:
        if isinstance(item, (int, float)):
            continue
        else:
            raise TypeError(f"Unsupported type {type(item)} found in volume measurements. Expected numeric types.")

    return max(volumes), min(volumes)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    sample_volumes = [10.5, 23.4, 8.9, 45.67, 12.3, 99.99]

    max_vol, min_vol = find_volume_extremes(sample_volumes)

    print(f"Maximum volume: {max_vol}")
    print(f"Minimum volume: {min_vol}")