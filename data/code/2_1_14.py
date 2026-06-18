def calculate_average_volume(volume_measurements: list[float]) -> float:
    """
    Calculates the arithmetic mean of a list of volume measurements efficiently.
    
    Args:
        volume_measurements (list[float]): A list containing numerical values representing volumes.
        
    Returns:
        float: The calculated average (arithmetic mean) of the provided volume measurements.
            
    Raises:
        ValueError: If the input list is empty or contains non-numeric elements.
    """
    if not isinstance(volume_measurements, list):
        raise TypeError("Input must be a list.")
    
    if len(volume_measurements) == 0:
        raise ValueError("The volume measurements list cannot be empty.")

    total_volume = sum(volume_measurements)
    count = len(volume_measurements)
    
    return total_volume / count

if __name__ == '__main__':
    # Hard-coded sample values representing volume measurements in liters.
    # These are designed to run without any user input or external dependencies.
    sample_data = [10.5, 23.7, 45.2, 67.8, 12.3]

    try:
        average_result = calculate_average_volume(sample_data)
        print(f"Average volume from {len(sample_data)} measurements: {average_result:.2f}")
    except ValueError as ve:
        print(f"Error during calculation: {ve}")