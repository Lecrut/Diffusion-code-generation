import math

def compare_lengths(val1: float, val2: float) -> tuple[float, str]:
    """
    Compares two floating-point numbers by their absolute length (magnitude).
    
    Args:
        val1: First floating-point number.
        val2: Second floating-point number.
        
    Returns:
        A tuple containing:
            - The absolute difference between the values as a float.
            - A string describing which value is greater in magnitude.
            
                If equal, returns "Both lengths are equal".
                Otherwise, indicates if 'val1' or 'val2' is longer than the other.
    """
    abs_diff = abs(val1 - val2)
    
    # Determine magnitudes using absolute values for comparison of length
    mag1 = abs(val1)
    mag2 = abs(val2)
    
    if math.isclose(mag1, mag2):
        description = "Both lengths are equal"
    elif mag1 > mag2:
        description = f"{val1} is greater than {val2}"
    else:
        description = f"{val2} is greater than {val1}"
        
    return abs_diff, description

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    a = 3.56789
    b = -4.01
    
    diff, desc = compare_lengths(a, b)
    
    print(f"Difference: {diff}")
    print(f"Comparison description: {desc}")