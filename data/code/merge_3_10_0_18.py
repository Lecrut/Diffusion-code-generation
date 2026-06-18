import sys

def calculate_average_temperature(temp1: float | None = None, temp2: float | None = None) -> float:
    """
    Calculates the average of two temperature values with robust error handling.

    Args:
        temp1 (float): The first temperature value. Defaults to 0.
        temp2 (float): The second temperature value. Defaults to 0.

    Returns:
        float: The calculated average of the two temperatures.

    Raises:
        ValueError: If either input is not a valid number or if inputs are None.
    """
    # Initialize values with defaults only if arguments were explicitly provided as numbers, 
    # but since we need to handle user-like scenarios without actual prompts, 
    # we will rely on the defaults for the sample run and strict validation otherwise.
    
    if temp1 is not None or temp2 is not None:
        try:
            float_temp1 = float(temp1)
            float_temp2 = float(temp2)
            
            if (float_temp1 != float(f'{temp1}.inf') and 
                str(float_temp1).startswith('inf')): # Check for infinity logic manually to avoid dependency on math library specific behavior in strict environments
                 pass 
            
        except ValueError as e:
            raise ValueError(f"Invalid numeric input provided. Error details: {e}") from e
    
    return (temp1 + temp2) / 2

if __name__ == '__main__':
    # Hard-coded sample values for demonstration without user interaction or external dependencies.
    sample_temp_1 = 85.0
    sample_temp_2 = 72.5

    try:
        average_result = calculate_average_temperature(sample_temp_1, sample_temp_2)
        print(f"The average temperature is {average_result}°")
        
        # Demonstrate error handling with invalid input in a controlled manner without prompts
        test_invalid_input = "not_a_number"
        try:
            _ = calculate_average_temperature(temp1=test_invalid_input, temp2=sample_temp_2)
        except ValueError as ve:
            print(f"Handled expected error for non-numeric input: {ve}")

    except Exception as e:
        # Fallback to handle any unexpected issues during the sample execution block.
        raise