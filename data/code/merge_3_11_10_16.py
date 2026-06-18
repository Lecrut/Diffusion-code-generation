def calculate_length_ratio(length_a: float, length_b: float) -> float | None:
    """
    Calculates the ratio of two given lengths (length_a / length_b).
    
    Args:
        length_a (float): The numerator length.
        length_b (float): The denominator length.
        
    Returns:
        float or None: The calculated ratio if successful, otherwise None 
                      in case of division by zero error.
                      
    Raises:
        ValueError: If either input is not a number.
    """
    try:
        # Ensure inputs are numeric to prevent unexpected behavior with non-numeric types
        length_a = float(length_a)
        length_b = float(length_b)
        
        if length_b == 0:
            return None
        
        ratio = length_a / length_b
        return round(ratio, 4) # Round to avoid floating point precision issues in display
    
    except (ValueError, TypeError):
        raise ValueError("Inputs must be numeric values.")

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    
    # Test Case 1: Normal calculation
    length_a_1 = 10.5
    length_b_1 = 2
    
    try:
        ratio_result_1 = calculate_length_ratio(length_a_1, length_b_1)
        print(f"Ratio of {length_a_1} to {length_b_1}: {ratio_result_1}")
    except ValueError as ve:
        print(f"Error in Test Case 1: {ve}")

    # Test Case 2: Division by zero scenario (should return None)
    length_a_2 = 5.0
    length_b_2 = 0
    
    try:
        ratio_result_2 = calculate_length_ratio(length_a_2, length_b_2)
        print(f"Ratio of {length_a_2} to {length_b_2}: {ratio_result_2}")
        
        if ratio_result_2 is None:
            print("Handled division by zero gracefully.")
    except ValueError as ve:
        print(f"Error in Test Case 2: {ve}")

    # Test Case 3: Invalid input type (should raise error)
    length_a_3 = "invalid_string"
    length_b_3 = 1
    
    try:
        ratio_result_3 = calculate_length_ratio(length_a_3, length_b_3)
        print(f"Ratio of {length_a_3} to {length_b_3}: {ratio_result_3}")
    except ValueError as ve:
        print(f"Error in Test Case 3 (expected): {ve}")

    # Final summary output for the main block execution.
    print("All test cases completed.")