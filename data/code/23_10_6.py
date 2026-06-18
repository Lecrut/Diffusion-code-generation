import math

def floats_equal(a: float, b: float) -> bool:
    """
    Compares two floating-point numbers for equality within a specified tolerance.
    
    This function uses the `math.isclose` method to determine if two floating-point 
    values are close enough in magnitude and relative difference to be considered equal.
    
    Parameters:
        a (float): The first float value to compare.
        b (float): The second float value to compare.
        
    Returns:
        bool: True if the numbers are within tolerance, False otherwise.
    """
    return math.isclose(a, b)

if __name__ == '__main__':
    # Sample test cases without user input
    
    # Case 1: Two values very close to each other (0 and small epsilon)
    val_a = 0.0
    val_b = 1e-9
    result_1 = floats_equal(val_a, val_b)
    
    # Case 2: Integers represented as floats that should be equal
    int_val = 5
    float_rep = float(int_val)
    result_2 = floats_equal(int_val, float_rep)
    
    # Case 3: Two distinct values far apart in magnitude
    large_diff_a = 10.0
    large_diff_b = 9876543.21
    
    # Calculate a relative tolerance to make the third case fail correctly 
    # because they are relatively very different despite absolute difference being non-zero.
    result_3 = floats_equal(large_diff_a, large_diff_b)
    
    print(f"Comparison {val_a} vs {val_b}: {result_1}")
    print(f"Comparison 5 vs 5.0: {result_2}")
    print(f"Comparison 10.0 vs 9876543.21: {result_3}")