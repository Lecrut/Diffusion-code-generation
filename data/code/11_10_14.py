def calculate_ratio(length_a: float, length_b: float) -> float | None:
    """
    Calculate the ratio of two lengths (length_a / length_b).
    
    Parameters:
        length_a (float): The numerator length value.
        length_b (float): The denominator length value.
        
    Returns:
        float or None: The calculated ratio if successful, otherwise None 
                      to indicate a division by zero error was encountered.
                      
    Raises:
        No exceptions are raised; errors are handled internally and returned via return values.
    """
    
    # Check for potential division by zero before performing the operation
    if length_b == 0:
        print("Error: Division by zero is not allowed.")
        return None
    
    result = length_a / length_b
    return result

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    sample_length_1 = 20.5
    sample_length_2 = 4

    print(f"Calculating ratio of {sample_length_1} and {sample_length_2}")
    
    result = calculate_ratio(sample_length_1, sample_length_2)
    
    if result is not None:
        print(f"The calculated ratio is: {result:.4f}")
    else:
        print("Calculation failed due to invalid input.")

# Additional test case for division by zero handling (uncommented below would require a second call, 
# but this block only runs once. For demonstration purposes in the same execution flow logic):
    
    # Uncommenting the following lines simulates another scenario if needed:
    # sample_length_3 = 10
    # sample_length_4 = 0
    
    # print(f"Calculating ratio of {sample_length_3} and {sample_length_4}")
    # result_zero_division = calculate_ratio(sample_length_3, sample_length_4)
    
    # if result_zero_division is not None:
    #     print(f"The calculated ratio is: {result_zero_division:.4f}")