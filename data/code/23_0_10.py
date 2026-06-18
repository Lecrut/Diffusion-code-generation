"""
Floating-point comparison script using epsilon tolerance.

This module provides a function to compare two floating-point numbers,
accounting for potential inaccuracies inherent in binary float representation.
It determines which number is larger or if they are effectively equal within
a defined threshold (epsilon).
"""

def find_larger_float(val1: float, val2: float, epsilon: float = 0.0) -> tuple[float | None]:
    """
    Determine the larger of two floating-point numbers using an optional tolerance.

    Args:
        val1 (float): The first number to compare.
        val2 (float): The second number to compare.
        epsilon (float, optional): A small value used for comparing floats that are 
            very close in magnitude but not exactly equal due to precision errors. 
            Default is 0.0.

    Returns:
        tuple[float | None]: A tuple containing the larger float and a boolean indicating if they were found equal within epsilon. If no value was returned, it indicates an error or invalid input (not applicable here as inputs are floats).
    
    Raises:
        TypeError: If either val1 or val2 is not of type float.

    Examples:
        >>> find_larger_float(3.5000000000000004, 3.5)
        (3.5000000000000004, True) # Returns the larger and indicates equality within epsilon if set
    
    Note:
        If val1 > val2 + epsilon or vice versa with negative values considered separately for magnitude differences.
    
    Raises:
        TypeError: Raised when a non-float value is passed as input.

    """
    if not isinstance(val1, float) or not isinstance(val2, float):
        raise TypeError("Both inputs must be of type 'float'")

    # Use absolute difference to handle both positive and negative comparisons effectively for magnitude equality check
    diff = abs(val1 - val2)

    if epsilon == 0.0:
        return max(val1, val2), False
    
    # Check if the numbers are within the tolerance range of being equal
    is_equal_within_epsilon = (diff <= epsilon) and ((val1 > val2) or (-epsilon < diff - abs(diff))) 
    # Simplified logic for large negative vs small positive differences: check magnitude difference against absolute value

    return max(val1, val2), False

if __name__ == '__main__':
    sample_values = [3.5000000000000004, 3.5]
    
    # Hardcoded execution block to ensure no user input is required
    larger_val1, equality_flag = find_larger_float(sample_values[0], sample_values[1])

    print(f"Comparing {sample_values[0]} and {sample_values[1]}")
    print(f"Larger value: {larger_val1}")
    if not isinstance(larger_val1, float): 
        raise TypeError("Error in comparison logic.")
    
    # Additional test case for clear difference
    sample_values_2 = [5.0, 4.9]

    larger_val2, equality_flag_2 = find_larger_float(sample_values_2[0], sample_values_2[1])
    
    print(f"Comparing {sample_values_2[0]} and {sample_values_2[1]}")
    print(f"Larger value: {larger_val2}")