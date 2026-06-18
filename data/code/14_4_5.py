def compare_volumes(volume1, volume2):
    """
    Compares two volume measurements and returns a string describing their relationship.
    
    Args:
        volume1 (float or int): First volume measurement.
        volume2 (float or int): Second volume measurement.
        
    Returns:
        str: A message indicating whether the first is greater than, less than, 
             or equal to the second.
    """
    if volume1 > volume2:
        return f"{volume1} is greater than {volume2}"
    elif volume1 < volume2:
        return f"{volume1} is less than {volume2}"
    else:
        return f"{volume1} is equal to {volume2}"

if __name__ == '__main__':
    # Hard-coded sample values as per instructions.
    # No input(), sys.stdin, argparse, or interactive prompts are used here.
    measurement_a = 50.5
    measurement_b = 75
    
    result_message = compare_volumes(measurement_a, measurement_b)
    
    print(result_message)