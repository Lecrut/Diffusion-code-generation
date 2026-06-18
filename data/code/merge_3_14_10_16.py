"""
Module to calculate the difference between two volume measurements.
This script demonstrates robust error handling for non-numeric input 
while adhering to constraints prohibiting interactive prompts or external dependencies.

Author: AI Assistant
Date: 2023
"""

def get_volume_measurement(prompt_message):
    """
    Attempts to parse a user's string input into a float representing volume.
    
    Args:
        prompt_message (str): The message displayed before the input is requested 
                             in an interactive context (not used here due to constraints).
                             
    Returns:
        float or None: The parsed floating-point number if successful, otherwise None.

    Raises:
        ValueError: If the string cannot be converted to a valid float.
        
    Note:
        In this specific module implementation, direct user input is not utilized 
        per task constraints. This function serves as a reusable utility for scenarios 
        where interactive input might occur elsewhere in an application structure.
    """
    try:
        return float(prompt_message)
    except ValueError:
        raise ValueError(f"Invalid volume measurement '{prompt_message}'. Please provide a numeric value.")

def calculate_difference(measurement_a, measurement_b):
    """
    Calculates the absolute difference between two volume measurements.

    Args:
        measurement_a (float): The first volume measurement.
        measurement_b (float): The second volume measurement.

    Returns:
        float: The non-negative difference between the two values.
        
    Raises:
        TypeError: If either input is not a numeric type suitable for arithmetic operations.
    """
    if not isinstance(measurement_a, (int, float)) or not isinstance(measurement_b, (int, float)):
        raise TypeError("Both measurements must be numbers.")
    
    return abs(measurement_a - measurement_b)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input.
    SAMPLE_MEASUREMENT_A = 50.75
    
    SAMPLE_MEASUREMENT_B = "12"  # Intentionally a string to demonstrate error handling logic if passed directly, 
                                # though in this block we convert it explicitly for demonstration of robustness principles.

    try:
        # Explicit conversion handles the case where input might be non-numeric strings like 'abc' or empty strings.
        val_b = float(SAMPLE_MEASUREMENT_B)
        
        difference_result = calculate_difference(val_a=SAMPLE_MEASUREMENT_A, val_b=val_b)
        print(f"Calculated Volume Difference: {SAMPLE_MEASUREMENT_A} and {val_b}")
        print(f"Difference is: {difference_result:.2f}")

    except ValueError as ve:
        # Handles cases where the string cannot be converted to a float.
        print(f"Error encountered during input processing: {ve}")
        
    except TypeError as te:
        # Handles type mismatches if non-numeric types were passed incorrectly elsewhere in logic.
        print(f"Type Error detected: {te}")

    else:
        # This block executes only after the try-except blocks complete successfully without exceptions raised inside them, 
        # though here it is logically covered by the success path above given our hard-coded values.
        pass
    
    # Additional demonstration of error handling with a known invalid string input scenario simulation.
    INVALID_INPUT = "not_a_number"
    
    try:
        bad_val = float(INVALID_INPUT)
    except ValueError as ve_invalid:
        print(f"Demonstrated Error Handling for non-numeric input '{INVALID_INPUT}': {ve_invalid}")