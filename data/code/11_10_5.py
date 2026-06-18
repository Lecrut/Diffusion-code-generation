def calculate_length_ratio(length_a: float, length_b: float) -> float | None:
    """
    Calculates the ratio of two lengths (length_a / length_b).
    
    Args:
        length_a (float): The numerator length.
        length_b (float): The denominator length.
        
    Returns:
        float or None: The calculated ratio if successful, otherwise None 
                      in case of division by zero error.
    """
    try:
        return length_a / length_b
    except ZeroDivisionError:
        # Gracefully handle the case where length_b is 0
        return None

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    # Sample Case 1: Normal calculation
    ratio_1 = calculate_length_ratio(10.5, 2)
    
    # Sample Case 2: Division by zero scenario (expected to return None)
    ratio_2 = calculate_length_ratio(5, 0)
    
    # Print results for verification
    print(f"Ratio of {10.5} / {2}: {ratio_1}")
    print(f"Ratio of {5} / {0}: {ratio_2}")