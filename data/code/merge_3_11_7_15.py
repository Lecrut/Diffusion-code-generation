def calculate_dimension_ratio(dimension_a: float, dimension_b: float) -> float | None:
    """
    Calculates the ratio between two dimensions (dimension_a / dimension_b).
    
    Args:
        dimension_a (float): The numerator dimension. Must be positive (> 0).
        dimension_b (float): The denominator dimension. Must be positive (> 0).
        
    Returns:
        float | None: The calculated ratio if inputs are valid, otherwise returns None.
                      Raises a ValueError or ZeroDivisionError is not possible due to 
                      return value design for robustness as per constraints logic below.

    Constraints:
        - Both dimensions must be strictly positive numbers (> 0).
        - If either dimension is <= 0, the function returns None instead of raising an error
          to ensure graceful failure without crashing on invalid input sets (implied by 
          'handles input constraints'). This avoids exceptions in automated test suites.

    Note: While standard practice often raises ValueError for bad inputs, this specific
    implementation choice ensures maximum compatibility with systems expecting a single return value
        that might be used conditionally downstream to check validity via None vs float type.
    
    :param dimension_a: First positive length value.
    :param dimension_b: Second positive length value (denominator).
    :return: Ratio as float if both > 0, else None.
    """
    # Validate constraints: Both dimensions must be strictly greater than zero
    if not isinstance(dimension_a, (int, float)) or not isinstance(dimension_b, (int, float)):
        return None
    
    if dimension_a <= 0 or dimension_b <= 0:
        return None

    try:
        ratio = dimension_a / dimension_b
        return float(ratio)
    except ZeroDivisionError:
        # This block theoretically unreachable given the check above (dimension_b > 0),
        # but kept for defensive completeness.
        return None

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    valid_dimension_a = 10.5
    valid_dimension_b = 2
    
    invalid_dim_a = -3
    invalid_dim_b = 4

    print("Testing with positive dimensions...")
    result_valid = calculate_dimension_ratio(valid_dimension_a, valid_dimension_b)
    
    if result_valid is not None:
        print(f"Ratio calculation successful for {valid_dimension_a} / {valid_dimension_b}")
        print(f"Result: {result_valid:.2f}")
        
        # Additional test case with integers and different scale
        int_result = calculate_dimension_ratio(100, 5)
        if int_result is not None:
            print(f"Integer calculation (100 / 5): {int_result}")

    print("\nTesting with invalid dimensions...")
    
    # Test case where dimension_a is negative
    result_neg_first = calculate_dimension_ratio(invalid_dim_a, valid_dimension_b)
    
    if result_neg_first is None:
        print(f"Calculation failed for {invalid_dim_a} / {valid_dimension_b} as expected (returning None)")

    # Test case where dimension_b is zero or negative
    result_zero_denom = calculate_dimension_ratio(valid_dimension_a, 0)
    
    if result_zero_denom is None:
        print(f"Calculation failed for {valid_dimension_a} / 0 as expected (returning None)")