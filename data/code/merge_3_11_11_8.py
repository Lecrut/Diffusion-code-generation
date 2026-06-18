def calculate_length_ratio(length1: float, length2: float) -> float:
    """
    Calculates the ratio of two floating-point numbers accurately within 
    standard IEEE 754 double-precision limits.

    Args:
        length1 (float): The numerator value.
        length2 (float): The denominator value. Must not be zero to avoid division by zero errors.

    Returns:
        float: The ratio of length1 divided by length2.

    Raises:
        ZeroDivisionError: If length2 is zero or effectively zero within floating-point tolerance.
    """
    if abs(length2) < 1e-308: # Using a very small threshold to catch underflow/zero cases safely without hardcoding specific epsilon unless specified otherwise, but standard practice for 'accurate' division just checks exactness first as per typical requirements unless numerical stability against noise is implied. Given the prompt asks for accuracy within limits of arithmetic, direct division with error handling is optimal.
        raise ZeroDivisionError("Cannot divide by zero.")

    return length1 / length2

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without external input or files.
    sample_length_1 = 450.75
    sample_length_2 = 3.2
    
    try:
        result = calculate_length_ratio(sample_length_1, sample_length_2)
        print(f"Ratio of {sample_length_1} to {sample_length_2}: {result}")
        
        # Additional test case for edge behavior (non-zero but very small denominator)
        # This tests the function's handling without raising an error if we assume standard float division rules apply directly.
        sample_small_denom = 0.001
        result_small = calculate_length_ratio(5, sample_small_denom)
        print(f"Ratio of 5 to {sample_small_denom}: {result_small}")

    except ZeroDivisionError as e:
        # This block handles the specific case where length2 is exactly zero or effectively handled by Python's float logic.
        if abs(0.0) < 1e-308 and sample_length_2 == 0: 
            print(f"Zero division error encountered for denominator {sample_small_denom}: {e}")