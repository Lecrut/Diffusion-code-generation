import math

def compare_measurements(length_a: float, length_b: float) -> tuple[float, str]:
    """
    Compares two given length measurements (floats representing meters).
    
    Args:
        length_a: First measurement value in meters.
        length_b: Second measurement value in meters.
        
    Returns:
        A tuple containing:
            - The difference between the two lengths (length_a - length_b) as a float.
            - A string indicating whether 'a' is greater than, less than, or equal to 'b'.
            
    Examples:
        compare_measurements(10.5, 10.5) -> (-0.0, "equal")
        compare_measurements(20.3, 15.7) -> (4.6, "greater")
        compare_measurements(8.0, 9.2) -> (-1.2, "less")
    """
    diff = length_a - length_b
    
    if abs(diff) < math.isclose(length_a, length_b):
        comparison_result = "equal"
    elif length_a > length_b:
        comparison_result = "greater"
    else:
        comparison_result = "less"
        
    return float(diff), comparison_result

if __name__ == '__main__':
    # Hard-coded sample values for testing without external input or files
    val1, result_name_1 = compare_measurements(50.25, 48.7)
    
    print(f"Measurement A: {val1:.2f} m")
    print(f"Comparison Result: {'greater' if result_name_1 == 'greater' else ('less' if result_name_1 == 'less' else 'equal')}")