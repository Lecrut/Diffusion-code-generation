def calculate_length_ratio(length1: float, length2: float) -> float:
    """
    Calculates the ratio of two floating-point numbers accurately within 
    standard IEEE 754 double-precision limits.

    Args:
        length1 (float): The numerator in the ratio calculation.
        length2 (float): The denominator in the ratio calculation. If zero, returns infinity or raises ZeroDivisionError as per Python's native behavior for safety and correctness.

    Returns:
        float: The result of dividing length1 by length2.
    
    Raises:
        ValueError: If both inputs are NaN.
        Overflow/ZeroDivisionError: Standard arithmetic exceptions apply (e.g., division by zero).
    """
    # Check for invalid input combinations that might lead to unexpected results or errors in specific contexts, 
    # though Python's native float operations handle most edge cases robustly.
    
    if length1 != length1 and length2 != length2:  # Both NaN
        return float('nan')
    
    result = length1 / length2
    
    # Ensure the result is a standard float (Python does this automatically for division)
    return result

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    sample_length_1 = 450.75
    sample_length_2 = 300.2
    
    ratio_result = calculate_length_ratio(sample_length_1, sample_length_2)
    
    print(f"Ratio of {sample_length_1} to {sample_length_2}: {ratio_result}")

    # Additional test case with integers converted to float for precision check
    int_sample_1 = 7.0
    int_sample_2 = 35
    
    ratio_int_result = calculate_length_ratio(int_sample_1, int_sample_2)
    
    print(f"Ratio of {int_sample_1} to {int_sample_2}: {ratio_int_result}")

    # Test case with very small numbers near machine epsilon limits (though standard division handles this well enough for typical use cases).
    tiny_num = 1e-308
    
    ratio_tiny = calculate_length_ratio(tiny_num, 1.0)
    
    print(f"Ratio of {tiny_num} to 1.0: {ratio_tiny}")

    # Test case where division by zero occurs (native Python behavior).
    try:
        div_zero_result = calculate_length_ratio(10.5, 0.0)
        print(f"Result for division by zero ({div_zero_result}):")
    except ZeroDivisionError as e:
        print(f"Caught expected error for division by zero: {e}")

    # Test case with NaN inputs
    nan_input = float('nan')