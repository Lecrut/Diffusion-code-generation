"""
Temperature Average Calculator Module

This module provides functionality to calculate the average of two temperature values.
It includes robust error handling for non-numeric inputs and ensures no external dependencies
or interactive prompts are used during execution.

Features:
    - Calculates the arithmetic mean of two temperatures.
    - Handles invalid input types gracefully with informative messages.
    - Includes a self-contained test block using hard-coded values.

Usage:
    Run this script directly to execute the sample calculation defined in the main block.
"""

def calculate_average_temperature(temp1, temp2):
    """
    Calculate and return the average of two temperature values.

    Args:
        temp1 (float or int): The first temperature value.
        temp2 (float or int): The second temperature value.

    Returns:
        float: The calculated average temperature.

    Raises:
        TypeError: If either input is not a numeric type (int, float).
    """
    if not isinstance(temp1, (int, float)) or not isinstance(temp2, (int, float)):
        raise TypeError(f"Both inputs must be numbers. Received {type(temp1).__name__} and {type(temp2).__name__}.")

    return (temp1 + temp2) / 2

def main():
    """
    Main execution block containing hard-coded sample values for testing.
    
    This function demonstrates the usage of calculate_average_temperature with 
    pre-defined numeric inputs, ensuring no user interaction or external dependencies are required.
    """
    # Hard-coded sample temperatures (e.g., 25 degrees Celsius and 30 degrees Celsius)
    temperature_a = 25.0
    temperature_b = 30.0

    try:
        average_temp = calculate_average_temperature(temperature_a, temperature_b)
        print(f"The average of {temperature_a}°C and {temperature_b}°C is {average_temp:.1f}°C.")
    except TypeError as e:
        # Although unlikely with hard-coded numbers, this handles potential type mismatches if changed later.
        print(f"Error during calculation: {e}")

if __name__ == '__main__':
    main()