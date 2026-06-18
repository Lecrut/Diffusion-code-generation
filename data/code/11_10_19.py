def calculate_length_ratio(length_a: float, length_b: float) -> float | None:
    """
    Calculate the ratio of two given lengths (length_a / length_b).
    
    Args:
        length_a (float): The numerator length.
        length_b (float): The denominator length.
        
    Returns:
        float or None: The calculated ratio if division is possible, 
                      otherwise None to indicate a potential error condition.
                      
    Raises:
        ValueError: If either input is not numeric.
    """
    try:
        # Ensure inputs are numbers
        num = float(length_a)
        den = float(length_b)
        
        if den == 0:
            return None
        
        return num / den
    except (ValueError, TypeError):
        raise ValueError("Inputs must be numeric values.")

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or network access.
    
    # Test Case 1: Normal division
    length_1 = 10.5
    length_2 = 3.0
    ratio_normal = calculate_length_ratio(length_1, length_2)
    print(f"Ratio of {length_1} and {length_2}: {ratio_normal}")

    # Test Case 2: Division by zero (handled gracefully)
    length_3 = 5.0
    length_4 = 0.0
    ratio_zero_denom = calculate_length_ratio(length_3, length_4)
    print(f"Ratio of {length_3} and {length_4}: {ratio_zero_denom}")

    # Test Case 3: Integer division result
    length_5 = 8
    length_6 = 2
    ratio_ints = calculate_length_ratio(length_5, length_6)
    print(f"Ratio of {length_5} and {length_6}: {ratio_ints}")

    # Test Case 4: Negative values (valid mathematical operation)
    length_7 = -10.0
    length_8 = 2.0
    ratio_negatives = calculate_length_ratio(length_7, length_8)
    print(f"Ratio of {length_7} and {length_8}: {ratio_negatives}")

    # Test Case 5: Invalid input type (intentionally omitted from execution to avoid runtime errors in this context, 
    # but the function handles it via exception raising if called directly).