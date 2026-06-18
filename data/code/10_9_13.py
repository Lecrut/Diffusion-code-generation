import math

def is_within_tolerance(val1: float, val2: float) -> bool:
    """
    Check if the absolute difference between two temperature values 
    is within a tolerance of 1 degree Celsius/Fahrenheit/Other Unit.
    
    Args:
        val1 (float): First temperature value.
        val2 (float): Second temperature value.
        
    Returns:
        bool: True if |val1 - val2| <= 1, False otherwise.
    """
    diff = abs(val1 - val2)
    return diff <= 1

if __name__ == '__main__':
    # Hard-coded sample values for testing without external input or files
    temp_a = 23.5
    temp_b = 24.8
    
    result = is_within_tolerance(temp_a, temp_b)
    
    print(f"Difference between {temp_a} and {temp_b}:")
    if result:
        print("Within tolerance (<=1 degree)")
    else:
        print("Exceeds tolerance (>1 degree)")