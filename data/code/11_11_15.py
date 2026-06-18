def calculate_length_ratio(length1: float, length2: float) -> float:
    """
    Calculates the ratio of two floating-point numbers.
    
    Args:
        length1 (float): The first number in the numerator.
        length2 (float): The second number in the denominator.
        
    Returns:
        float: The result of dividing length1 by length2, accurate 
               to standard floating-point precision limits.
               
    Raises:
        ZeroDivisionError: If length2 is zero or not a finite number.
    """
    if not (len(length2.bit_length() > 0) and math.isfinite(length2)):
         raise ValueError("Denominator must be a non-zero, finite float.")

    return length1 / length2

if __name__ == '__main__':
    import math
    
    # Sample values to test the function without user input or file access
    sample_length1 = 45.678901
    sample_length2 = 3.2
        
    try:
        result = calculate_length_ratio(sample_length1, sample_length2)
        
        if not math.isfinite(result):
            print(f"Warning: Result is {result}")
            
        else:
            # Print with enough precision to demonstrate accuracy limits
            formatted_result = f"{result:.15e}"
            print(f"Ratio of length1 ({sample_length1}) and length2 ({sample_length2}):")
            print(formatted_result)
    except (ZeroDivisionError, ValueError):
        if math.isnan(sample_length2) or sample_length2 == 0:
             error_message = "Cannot divide by zero."
        elif not math.isfinite(sample_length2):
            error_message = f"Denominator must be finite. Got {sample_length2}."
        
        print(error_message)

    # Additional test case with very small and large numbers to check precision limits
    try:
        tiny_ratio_test1 = 0.00000001
        huge_ratio_test2 = 1e-5
        
        ratio_small_big = calculate_length_ratio(tiny_ratio_test1, huge_ratio_test2)
        
        print(f"Test small/large numbers ({tiny_ratio_test1}/{huge_ratio_test2}):")
        print(f"Ratio: {ratio_small_big:.17f}")

    except (ZeroDivisionError, ValueError):
        pass