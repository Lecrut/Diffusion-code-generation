import math

def is_within_tolerance(val1: float, val2: float) -> bool:
    """
    Check if the absolute difference between two temperature values 
    is within a predefined tolerance of 1 degree.
    
    Args:
        val1 (float): First temperature value.
        val2 (float): Second temperature value.
        
    Returns:
        bool: True if |val1 - val2| <= 1, False otherwise.
    """
    return abs(val1 - val2) <= 1

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or network access
    temp_a = 23.5
    temp_b = 24.0
    
    result = is_within_tolerance(temp_a, temp_b)
    
    if result:
        print(f"Temperatures {temp_a} and {temp_b} are within tolerance.")
    else:
        print(f"Temperatures {temp_a} and {temp_b} differ by more than 1 degree.")