def calculate_volume_difference(vol1: float, vol2: float) -> str:
    """
    Calculates the absolute difference between two volume measurements 
    and returns it formatted to two decimal places as a string.
    
    Args:
        vol1 (float): First volume measurement.
        vol2 (float): Second volume measurement.
        
    Returns:
        str: Absolute difference rounded to two decimal places.
    """
    return f"{abs(vol1 - vol2):.2f}"

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input)
    measurement_a = 45.678
    measurement_b = 30.129
    
    result = calculate_volume_difference(measurement_a, measurement_b)
    print(result)