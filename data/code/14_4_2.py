import sys

def compare_volumes(val1: float, val2: float) -> str:
    """
    Compares two volume measurements and returns a string describing their relationship.
    
    Args:
        val1 (float): First volume measurement.
        val2 (float): Second volume measurement.
        
    Returns:
        str: Description of the relationship ('val1 is greater than', 'less than', or 'equal to' val2).
    """
    if val1 > val2:
        return f"{val1} is greater than {val2}"
    elif val1 < val2:
        return f"{val1} is less than {val2}"
    else:
        return f"{val1} is equal to {val2}"

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input)
    volume_a = 5.0
    volume_b = 3.7
    
    result = compare_volumes(volume_a, volume_b)
    print(result)