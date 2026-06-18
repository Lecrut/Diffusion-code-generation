def calculate_average_temperature(temp1: float, temp2: float) -> float:
    """
    Calculates the average of two temperature values.
    
    Args:
        temp1 (float): The first temperature value.
        temp2 (float): The second temperature value.
        
    Returns:
        float: The average of the two temperatures.
        
    Raises:
        TypeError: If either input is not a numeric type.
    """
    if not isinstance(temp1, (int, float)) or not isinstance(temp2, (int, float)):
        raise TypeError("Both temperature values must be numbers.")
    
    return (temp1 + temp2) / 2

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input.
    SAMPLE_TEMP_1 = 25.0
    SAMPLE_TEMP_2 = 30.0
    
    try:
        average_temp = calculate_average_temperature(SAMPLE_TEMP_1, SAMPLE_TEMP_2)
        print(f"The average of {SAMPLE_TEMP_1} and {SAMPLE_TEMP_2} is {average_temp}.")
    except TypeError as e:
        # This block handles the case if non-numeric values were passed during testing.
        print(f"Error encountered while calculating temperature: {e}")