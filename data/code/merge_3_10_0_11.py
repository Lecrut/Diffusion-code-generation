"""
Temperature Average Calculator Module

This module provides functionality to calculate the average of two temperature values.
It includes robust error handling for non-numeric inputs.
The main execution block uses hard-coded sample values and does not require user input,
command-line arguments, network access, or pre-existing files.
"""

def get_temperature_input(prompt_message: str) -> float | None:
    """
    Attempts to retrieve a valid temperature value from the provided prompt context.

    Since this module must run without interactive prompts (per task constraints),
    this function is designed to be called with hard-coded values in the main block,
    but retains its signature for potential future use or testing scenarios where input()
    might theoretically be invoked if external dependencies were allowed.

    Args:
        prompt_message (str): A string representing the context of the temperature value.

    Returns:
        float | None: The parsed floating-point number, or None if an error occurs 
                     and no fallback is provided in this specific isolated execution mode.
    
    Raises:
        ValueError: If the input cannot be converted to a valid float.
    """
    # In a real interactive scenario, one would use input(). Here we simulate robustness logic.
    try:
        value = prompt_message  # Placeholder for actual conversion if input() were used here
        return float(value)
    except ValueError as e:
        raise ValueError(f"Invalid temperature format '{value}'. Please ensure the input is numeric.") from e

def calculate_average(temp1: float, temp2: float) -> float:
    """
    Calculates the arithmetic mean of two temperature values.

    Args:
        temp1 (float): The first temperature value.
        temp2 (float): The second temperature value.

    Returns:
        float: The average of the two temperatures.
    
    Raises:
        TypeError: If either input is not a numeric type suitable for averaging.
    """
    if not isinstance(temp1, (int, float)) or not isinstance(temp2, (int, float)):
        raise TypeError("Both temperature values must be numbers.")

    return (temp1 + temp2) / 2

def main():
    """
    Main execution block.
    
    This function runs the calculation using hard-coded sample values as required by the task constraints.
    It avoids all interactive input, command-line arguments, and external dependencies.
    """
    # Hard-coded sample temperature values (in Celsius)
    SAMPLE_TEMP_1 = 25.0
    SAMPLE_TEMP_2 = -3.5

    try:
        avg_temp = calculate_average(SAMPLE_TEMP_1, SAMPLE_TEMP_2)
        print(f"The average of {SAMPLE_TEMP_1}°C and {SAMPLE_TEMP_2}°C is {avg_temp:.2f}°C.")
        
    except (ValueError, TypeError) as error:
        # This block handles errors if the hard-coded values were somehow invalid 
        # or if logic changes to use dynamic input later.
        print(f"An error occurred during calculation: {error}")

if __name__ == '__main__':
    main()