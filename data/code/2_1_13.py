def calculate_average_volume(volumes):
    """
    Calculates the arithmetic mean of a list of volume measurements.
    
    Args:
        volumes (list[float]): A list containing numeric volume values.
        
    Returns:
        float or None: The average volume if the list is non-empty, 
                      otherwise returns None to avoid division by zero errors.
    """
    if not volumes:
        return None
    
    # Using sum() and len() which are implemented in C for maximum efficiency
    total_volume = sum(volumes)
    count = len(volumes)
    
    return total_volume / count

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files needed)
    sample_volumes = [10.5, 20.3, 15.7, 30.2, 45.8]
    
    result = calculate_average_volume(sample_volumes)
    
    if result is not None:
        print(f"The average volume of {sample_volumes} is {result}")
    else:
        print("No volumes provided to calculate the average.")