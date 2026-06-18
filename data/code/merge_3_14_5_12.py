def calculate_volume_difference(vol1: float, vol2: float) -> str:
    """
    Calculates the absolute difference between two volume measurements 
    and returns it formatted to two decimal places as a string.
    
    Args:
        vol1 (float): First volume measurement.
        vol2 (float): Second volume measurement.
        
    Returns:
        str: Absolute difference formatted to two decimal places.
    """
    absolute_difference = abs(vol1 - vol2)
    return f"{absolute_difference:.2f}"

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    measurement_a = 50.789
    measurement_b = 32.456
    
    result = calculate_volume_difference(measurement_a, measurement_b)
    
    print("Absolute difference:", result)