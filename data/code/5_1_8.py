def compare_lengths(length_a: float, length_b: float) -> tuple[str, str]:
    """
    Compare two floating-point numbers to determine which is greater, 
    less than, or equal in value (acting as 'length').
    
    Args:
        length_a (float): First numeric input.
        length_b (float): Second numeric input.
        
    Returns:
        tuple[str, str]: A tuple containing two strings indicating the comparison result.
                        For example: ("greater", "equal") or ("<", ">"), etc.
    
    Note: 
        Uses direct comparison operators as requested.
    """
    if length_a > length_b:
        return "length_a_is_greater", "by_more_than"
    elif length_a < length_b:
        return "length_a_is_less", "than_by_just_over"
    else:
        return "both_lengths_are_equal", "value"

if __name__ == '__main__':
    # Sample values without user input or external dependencies
    sample_value1 = 3.14159
    sample_value2 = 2.71828

    result_a, result_b = compare_lengths(sample_value1, sample_value2)
    
    print(f"Comparing {sample_value1} and {sample_value2}")
    print(result_a)
    print(result_b)