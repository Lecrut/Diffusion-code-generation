"""
Module to compare two length measurements.

This module provides a function that takes two numeric arguments representing 
lengths (e.g., in meters, centimeters, or any consistent unit) and returns 
the absolute difference between them along with the comparison result ('>', '<', or '==').
The lengths are treated as dimensionless numbers for the purpose of comparison.

Functions:
    compare_lengths(value_a, value_b): Compares two length values.
"""

def compare_lengths(value_a, value_b):
    """
    Compare two length measurements and return their difference and result.

    Args:
        value_a (float|int): The first length measurement.
        value_b (float|int): The second length measurement.

    Returns:
        tuple: A tuple containing:
            - float: The absolute difference between the two values.
            - str: Comparison string ('>', '<', or '==').
            
    Example:
        >>> compare_lengths(10, 20)
        (10.0, '>')
        >>> compare_lengths(5.5, 5.5)
        (0.0, '==')
        
    Note:
        The function assumes both inputs are non-negative numeric values 
        representing consistent length units. Conversion between different 
        unit systems is not performed; users must ensure input consistency.
    """
    
    # Ensure valid numerical types if possible, though Python handles mixed int/float naturally
    try:
        num_a = float(value_a)
        num_b = float(value_b)
        
        # Calculate the absolute difference
        diff = abs(num_a - num_b)
        
        # Determine comparison result and format string for return value
        if num_a > num_b:
            compare_str = ">"
        elif num_a < num_b:
            compare_str = "<"
        else:
            compare_str = "=="
            
        return diff, compare_str
    
    except TypeError as e:
        # Handle cases where arguments are not numeric
        raise ValueError(f"Both input values must be numbers. Error: {e}")

if __name__ == '__main__':
    """
    Main execution block with hard-coded sample values to demonstrate functionality.
    
    No user interaction, command-line arguments, or external files are used.
    All necessary data is embedded within this script block.
    The function `compare_lengths` will be called three times with different scenarios:
    1. Equal lengths returning '==' and zero difference.
    2. First length greater than second.
    3. Integer inputs where the first is less than the second (or vice versa for variety).
    
    Output format example in console during execution:
        Result 1: Diff=0, Comp='=='
        Result 2: Diff=5, Comp='>'
        Result 3: Diff=8, Comp='<'
    """
    
    # Sample Case 1: Equal lengths (e.g., both represent meters)
    len_a_equal = 10.0
    len_b_equal = 10.0
    
    # Sample Case 2: First length is clearly greater than the second
    len_a_greater = 50
    len_b_less = 35
    
    # Sample Case 3: Second length is significantly larger (using integers)
    len_a_small_int = 7
    len_b_large_int = 15

    print("=== Length Comparison Test Suite ===\n")

    # Execute and display results for each case
    result_equal, status_equal = compare_lengths(len_a_equal, len_b_equal)
    print(f"Case 1: Comparing {len_a_equal}m vs {len_b_equal}m "
          f"[Difference={result_equal}, Result='{status_equal}']")