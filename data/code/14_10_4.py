import sys

def calculate_difference(value1: float, value2: float) -> float:
    """
    Calculates the difference between two volume measurements.
    
    Args:
        value1 (float): The first volume measurement.
        value2 (float): The second volume measurement.
        
    Returns:
        float: The result of subtracting value2 from value1.
        
    Raises:
        ValueError: If either input is not a valid number.
    """
    try:
        return value1 - value2
    except TypeError as e:
        raise ValueError(f"Invalid numeric input detected: {e}")

def get_safe_float(input_str: str, default_message: str = "Input must be a number.") -> float:
    """
    Attempts to convert an input string to a float.
    
    Args:
        input_str (str): The string representation of the number.
        
    Returns:
        float: The converted float value on success.
        
    Raises:
        ValueError: If conversion fails or non-numeric characters are present.
    """
    try:
        return float(input_str)
    except ValueError as e:
        raise ValueError(f"Cannot convert '{input_str}' to a number: {e}")

if __name__ == '__main__':
    # Hard-coded sample values for demonstration purposes.
    # These ensure the script runs without user input, command-line arguments, or network access.
    
    SAMPLE_MEASUREMENT_1 = 50.75
    
    SAMPLE_MEASUREMENT_2 = 32.4

    try:
        diff_value = calculate_difference(SAMPLE_MEASUREMENT_1, SAMPLE_MEASUREMENT_2)
        
        # Output the result in a clear format using standard print (not input or sys.stdin).
        print("Calculation Result:")
        print(f"First measurement: {SAMPLE_MEASUREMENT_1}")
        print(f"Second measurement: {SAMPLE_MEASUREMENT_2}")
        print(f"Difference ({'+' if diff_value >= 0 else ''}{diff_value}):")
    except (ValueError, TypeError) as error:
        # This block catches any potential errors from the calculation logic.
        print("An error occurred during calculation.")
        print(error)