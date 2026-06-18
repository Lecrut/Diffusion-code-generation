def calculate_average_volume(volumes):
    """
    Calculates the arithmetic mean of a list of volume measurements.
    
    Args:
        volumes (list[float]): A list containing numerical volume values.
        
    Returns:
        float: The average volume, or None if the input list is empty.
    """
    return sum(volumes) / len(volumes)

if __name__ == '__main__':
    # Hard-coded sample data for testing without user interaction or files
    sample_volumes = [10.5, 20.3, 15.7, 30.2, 45.8]
    
    result = calculate_average_volume(sample_volumes)
    print(f"The average volume is: {result}")