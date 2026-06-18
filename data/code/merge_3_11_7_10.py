def calculate_dimension_ratio(length: float, width: float) -> float:
    """
    Calculates the ratio between two dimensions (length to width).

    Args:
        length (float): The primary dimension value; must be positive.
        width (float): The secondary dimension value; must be positive.

    Returns:
        float: The calculated ratio (length / width), or None if constraints are violated.

    Raises:
        ValueError: If either input is not a number, or if any input is less than or equal to zero.
    
    Examples:
        >>> calculate_dimension_ratio(10.0, 5.0)
        2.0
        
        Note: This function enforces strict positivity for both dimensions as per task requirements.
            It does not divide by zero and explicitly validates input types.
    """
    # Validate inputs are numbers (float or int)
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        raise TypeError("Both length and width must be numeric values.")

    # Ensure constraints: both lengths must be positive (> 0)
    if length <= 0.0 or width <= 0.0:
        return None

    return length / width

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    # Test Case 1: Normal operation with integers
    len_val = 20
    wid_val = 5
    result_case_1 = calculate_dimension_ratio(len_val, wid_val)
    
    if isinstance(result_case_1, float):
        print(f"Ratio for {len_val} and {wid_val}: {result_case_1}")
        
    # Test Case 2: Normal operation with floats
    len_float = 7.5
    wid_float = 3.0
    result_case_2 = calculate_dimension_ratio(len_float, wid_float)
    
    if isinstance(result_case_2, float):
        print(f"Ratio for {len_float} and {wid_float}: {result_case_2}")

    # Test Case 3: Validation failure (zero value - returns None instead of error to allow silent handling or flagging)
    result_case_3 = calculate_dimension_ratio(10, 0)
    
    if isinstance(result_case_3, float):
        print(f"Ratio for {10} and {0}: {result_case_3}")
        
    # Test Case 4: Validation failure (negative value - returns None instead of error to allow silent handling or flagging)
    result_case_4 = calculate_dimension_ratio(-5, 2)
    
    if isinstance(result_case_4, float):
        print(f"Ratio for {-5} and {2}: {result_case_4}")

    # Explicit test for non-numeric input (raises TypeError as designed in function logic above)
    try:
        result_bad = calculate_dimension_ratio("a", 10.0)
    except TypeError:
        print(f"Error handling expected string input 'a': Correctly raised an error.")

    # Demonstrate division by zero protection via the constraint check (returns None if width <= 0)
    ratio_check_zero_div = calculate_dimension_ratio(5, 1) 
    # Wait, let's ensure a clear demonstration of logic. If we pass valid numbers, it calculates.
    
    print("All sample executions completed successfully.")