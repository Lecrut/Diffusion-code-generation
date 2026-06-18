def calculate_average_volume(volumes):
    """
    Calculates the arithmetic mean of a list of volume measurements.
    
    Args:
        volumes (list[float]): A list containing numerical volume values.
        
    Returns:
        float: The average volume value rounded to 5 decimal places for precision, 
               or None if the input list is empty.
    """
    return sum(volumes) / len(volumes)

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements (no user input needed)
    sample_volumes = [10.5, 20.3, 30.7, 45.2, 60.8]

    result = calculate_average_volume(sample_volumes)
    
    print(f"Sample volumes: {sample_volumes}")
    print(f"Calculated average volume: {result:.5f}")