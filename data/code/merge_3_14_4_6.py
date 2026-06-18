def compare_volumes(val1: float, val2: float) -> str:
    """
    Compares two volume measurements and returns a string describing their relationship.
    
    Args:
        val1 (float): First volume measurement.
        val2 (float): Second volume measurement.
        
    Returns:
        str: A message indicating if the first value is greater, less than, or equal to 
             the second value.
    """
    if val1 > val2:
        return f"{val1} is greater than {val2}"
    elif val1 < val2:
        return f"{val1} is less than {val2}"
    else:
        return f"{val1} is equal to {val2}"

if __name__ == '__main__':
    # Hard-coded sample values as per requirements.
    volume_a = 50.5
    volume_b = 48.3
    
    result_message = compare_volumes(volume_a, volume_b)
    
    print(f"Comparing {volume_a} and {volume_b}:")
    print(result_message)