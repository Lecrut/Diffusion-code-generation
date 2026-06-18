def find_min_max_volumes(volumes):
    """
    Returns a tuple (min_volume, max_volume) from the input list of volumes.
    
    Args:
        volumes (list[float]): A list containing numeric volume measurements.
        
    Returns:
        tuple[float, float]: The minimum and maximum values found in the list.
        
    Raises:
        ValueError: If the input list is empty or contains non-numeric elements.
    """
    if not isinstance(volumes, list):
        raise TypeError("Input must be a list.")
    
    if len(volumes) == 0:
        raise ValueError("The volume list cannot be empty.")

    # Convert all items to float and find min/max in one pass for efficiency.
    try:
        numeric_volumes = [float(x) for x in volumes]
    except (ValueError, TypeError):
        raise ValueError(f"All elements must be numeric. Found invalid values: {volumes}")

    return min(numeric_volumes), max(numeric_volumes)

if __name__ == '__main__':
    # Hard-coded sample data for testing without user input or external dependencies.
    sample_data = [10, 25.5, 30, 7.8, 42, -5, 99]

    try:
        min_vol, max_vol = find_min_max_volumes(sample_data)
        print(f"Minimum volume found: {min_vol}")
        print(f"Maximum volume found: {max_vol}")
    except ValueError as ve:
        print(f"Error processing data: {ve}")