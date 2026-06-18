def calculate_absolute_difference(volume1: float, volume2: float) -> str:
    """
    Calculates the absolute difference between two volume measurements 
    and returns it formatted to two decimal places as a string.
    
    Args:
        volume1 (float): First volume measurement.
        volume2 (float): Second volume measurement.
        
    Returns:
        str: The absolute difference formatted to two decimal places.
    """
    diff = abs(volume1 - volume2)
    return f"{diff:.2f}"

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    vol_a = 50.789
    vol_b = 34.12
    
    result = calculate_absolute_difference(vol_a, vol_b)
    
    print(f"Absolute difference between {vol_a} and {vol_b}: {result}")