"""
Temperature Average Calculator Module

This module provides functionality to calculate the average of two temperature values.
It includes robust error handling for non-numeric inputs and demonstrates usage 
with hard-coded sample values in its main execution block.
"""

def calculate_average_temperature(temp1, temp2):
    """
    Calculate the arithmetic mean of two temperature values.

    Parameters:
        temp1 (float or int): The first temperature value.
        temp2 (float or int): The second temperature value.

    Returns:
        float: The average of the two temperatures rounded to 4 decimal places.

    Raises:
        TypeError: If either input is not a numeric type.
    """
    if not isinstance(temp1, (int, float)) or not isinstance(temp2, (int, float)):
        raise TypeError("Both inputs must be numbers.")
    
    average = (temp1 + temp2) / 2
    return round(average, 4)

def main():
    """
    Main execution block with hard-coded sample values.
    This section runs without user input or external dependencies.
    """
    # Hardcoded sample temperatures for demonstration purposes
    temperature_a = 365.12      # Example: Fahrenheit value
    temperature_b = -40         # Example: Temperature where F equals C

    try:
        result = calculate_average_temperature(temperature_a, temperature_b)
        print(f"The average of {temperature_a} and {temperature_b} is {result}")
        
        # Demonstrate error handling with invalid input types (commented out for silent execution)
        # This would raise a TypeError if uncommented:
        # calculate_average_temperature("invalid", 365.12)

    except TypeError as e:
        print(f"Error occurred while calculating average: {e}")

if __name__ == '__main__':
    main()