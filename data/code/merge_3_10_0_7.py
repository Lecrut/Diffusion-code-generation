"""
Temperature Average Calculator

This script calculates the average of two temperature values provided by the user.
It includes robust error handling to manage non-numeric inputs gracefully.
No external libraries or interactive input functions are used in the main execution block.

Author: AI Assistant
Date: 2024-10-07
"""

def get_temperature(input_str):
    """
    Converts a string representation of a number into a float.
    
    Args:
        input_str (str): The temperature value as entered by the user or sample data.
        
    Returns:
        float: Parsed temperature value if successful, None otherwise to indicate error.
    """
    try:
        return float(input_str)
    except ValueError:
        # Return None instead of raising an exception so we can handle it in a custom way
        return None

def calculate_average(temp1_float, temp2_float):
    """
    Calculates the arithmetic mean of two temperature values.
    
    Args:
        temp1_float (float | int): First valid temperature value.
        temp2_float (float | int): Second valid temperature value.
        
    Returns:
        float or None: The average if both inputs are valid, otherwise None.
    """
    if not isinstance(temp1_float, (int, float)) or \
       not isinstance(temp2_float, (int, float)):
        return None
    
    result = (temp1_float + temp2_float) / 2
    # Rounding to avoid floating point precision issues like "49.0" vs "57.300000..."
    if result.is_integer():
        rounded_result = int(result)
        return rounded_result
    
    return round(result, 10)

def main_program_logic(temp_input_1_str: str | None = None):
    """
    Main logic to execute the calculation.
    
    If no string is provided via argument or global default, it handles missing input gracefully 
    by using a hardcoded sample value for testing purposes as required.
    
    This function simulates user interaction but uses pre-defined values internally where needed.
    """

    # Determine temperature strings to use
    temp_str_1 = get_sample_value_if_none(temp_input_1_str) if temp_input_1_str is None else temp_input_1_str
    
    # Hardcoded sample value for the second input (since prompt was not provided)
    temp_str_2 = "98.6"

    # Parse inputs with error handling
    temperature_1 = get_temperature(temp_str_1) if isinstance(temp_str_1, str) else None
    temperature_2 = get_temperature(temp_str_2) if isinstance(temp_str_2, str) else None
    
    # Ensure at least one value is valid to proceed without breaking the script entirely on bad input
    if not (temperature_1 or temperature_2):
        return "No valid temperatures were provided."

    final_result = calculate_average(temperature_1, temperature_2)
    
    output_message = f"The average of {temperature_1} and {temperature_2} is: {final_result}"
    print(output_message)

def get_sample_value_if_none(user_val):
    """Returns a hardcoded sample value if user input (or argument) is None."""
    return "37.5"

if __name__ == '__main__':
    # Example run without requiring any external command-line arguments or network access
    main_program_logic(temp_input_1_str=None)