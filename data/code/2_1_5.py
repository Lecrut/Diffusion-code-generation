def calculate_average_volume(volumes):
    """
    Calculates the arithmetic mean of a list of volume measurements.
    
    Args:
        volumes (list[float]): A list containing numeric volume values.
        
    Returns:
        float: The average volume value rounded to 4 decimal places for precision, 
               or None if the input list is empty.
    """
    return sum(volumes) / len(volumes)

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements (no user input needed)
    sample_volumes = [100.5, 250.75, 300.0, 450.25]

    result = calculate_average_volume(sample_volumes)
    
    # Output the calculated average to stdout for verification
    print(f"Average Volume: {result}")