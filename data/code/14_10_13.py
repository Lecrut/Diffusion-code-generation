def calculate_volume_difference(volume_a: float, volume_b: float) -> float:
    """
    Calculates the absolute difference between two volume measurements.
    
    Args:
        volume_a (float): The first volume measurement.
        volume_b (float): The second volume measurement.
        
    Returns:
        float: The absolute difference between the two volumes.
    """
    return abs(volume_a - volume_b)

def validate_numeric_input(value_str: str) -> bool:
    """
    Validates if a string can be converted to a numeric value (int or float).
    
    Args:
        value_str (str): The input string to validate.
        
    Returns:
        bool: True if the string is valid, False otherwise.
    """
    try:
        float(value_str)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    # Hard-coded sample values as per requirements to avoid interactive input() or sys.stdin usage.
    SAMPLE_VOLUME_A = 10.5
    SAMPLE_VOLUME_B = 7.2
    
    result = calculate_volume_difference(SAMPLE_VOLUME_A, SAMPLE_VOLUME_B)
    
    print(f"Difference between {SAMPLE_VOLUME_A} and {SAMPLE_VOLUME_B}: {result}")