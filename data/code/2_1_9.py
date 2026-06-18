def calculate_average_volume(volumes):
    """
    Calculates the arithmetic mean of a list of volume measurements.
    
    Args:
        volumes (list[float]): A list containing numerical values representing 
                              volume measurements.
        
    Returns:
        float: The average value of the input list.
        
    Raises:
        ValueError: If the input list is empty or contains non-numeric elements.
    """
    if not isinstance(volumes, (list, tuple)):
        raise TypeError("Input must be a list or tuple.")
    
    try:
        total = sum(float(x) for x in volumes)
        return total / len(volumes)
    except ValueError as e:
        raise ValueError(f"Cannot calculate average due to invalid data type: {e}")

if __name__ == '__main__':
    # Hard-coded sample values representing volume measurements (in liters)
    sample_volumes = [10.5, 23.7, 45.2, 67.8, 90.1]

    try:
        average_volume = calculate_average_volume(sample_volumes)
        print(f"The calculated average volume is: {average_volume}")
    except ValueError as ve:
        print(f"Error during calculation: {ve}")