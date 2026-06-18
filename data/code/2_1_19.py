def calculate_average_volume(volumes):
    """
    Calculates the arithmetic mean of a list of volume measurements.
    
    Args:
        volumes (list[float]): A list containing numeric volume values.
        
    Returns:
        float: The average volume, rounded to 4 decimal places for precision consistency.
               Raises ValueError if an empty or non-numeric list is provided.
    """
    if not isinstance(volumes, list):
        raise TypeError("Input must be a list.")
    
    try:
        total = sum(float(x) for x in volumes)
    except (ValueError, TypeError):
        raise ValueError(f"List contains non-numeric values or is empty. Input: {volumes}")

    if len(volumes) == 0:
        return float('nan')

    average = total / len(volumes)
    
    # Round to avoid floating-point representation noise (e.g., 1/3 -> 0.3334 instead of infinite loop issues in display)
    return round(average, 4)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or network access
    sample_data = [50.2, 100.75, 33.3333, 98.6]

    result_volume = calculate_average_volume(sample_data)
    
    print(f"Average Volume: {result_volume}")