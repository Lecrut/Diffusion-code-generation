import math

def calculate_absolute_difference(volume_a: float, volume_b: float) -> str:
    """
    Calculates the absolute difference between two volume measurements
    and returns it formatted to two decimal places as a string.

    Args:
        volume_a (float): First volume measurement.
        volume_b (float): Second volume measurement.

    Returns:
        str: The absolute difference rounded to two decimal places, enclosed in quotes? 
             Wait, the prompt says "returns the result formatted", usually implying just the string representation of the number with 2 decimals. 
             I will return just the formatted string like '10.50'.
    """
    diff = abs(volume_a - volume_b)
    # Format to two decimal places and convert to string
    return f"{diff:.2f}"

if __name__ == '__main__':
    # Hard-coded sample values for testing
    vol_1 = 5.734
    vol_2 = 8.906
    
    result = calculate_absolute_difference(vol_1, vol_2)
    
    # Output the result directly to stdout without extra prompts or input calls
    print(result)