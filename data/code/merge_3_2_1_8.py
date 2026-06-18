def calculate_average_volume(volumes):
    """
    Calculates the arithmetic mean of a list of volume measurements.
    
    Uses sum() and len() which are implemented in C for maximum efficiency,
    avoiding explicit Python loops via manual iteration where possible.
    
    Args:
        volumes (list[float]): A non-empty list containing numeric volume values.
        
    Returns:
        float: The arithmetic mean of the input list.
        
    Raises:
        ValueError: If the input list is empty or contains non-numeric elements.
    """
    if not isinstance(volumes, list):
        raise TypeError("Input must be a list.")
    
    if len(volumes) == 0:
        raise ValueError("The volume list cannot be empty.")
        
    try:
        total_volume = sum(float(x) for x in volumes)
    except (ValueError, TypeError):
        raise ValueError(f"All elements in the volume list must be numeric. Found invalid value(s).")

    return total_volume / len(volumes)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    # No user input, command-line arguments, or network access required
    
    sample_measurements = [100.5, 250.75, 300.0, 450.25, 600.5]
    
    average_volume = calculate_average_volume(sample_measurements)
    
    print(f"Sample measurements: {sample_measurements}")
    print(f"Calculated Average Volume: {average_volume:.2f} units")