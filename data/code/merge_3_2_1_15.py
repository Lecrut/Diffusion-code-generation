def calculate_average_volume(volumes):
    """
    Calculates the arithmetic mean of a list of volume measurements.
    
    Args:
        volumes (list[float]): List containing numeric volume values.
        
    Returns:
        float or None: The average if the list is non-empty, otherwise None.
    """
    if not volumes:
        return None
    
    total_volume = sum(volumes)
    count = len(volumes)
    
    return total_volume / count

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    sample_data = [10.5, 20.3, 30.7, 40.1, 50.9]
    
    average_result = calculate_average_volume(sample_data)
    
    if average_result is not None:
        print(f"The calculated average volume is: {average_result}")
    else:
        print("No data provided to calculate the average.")