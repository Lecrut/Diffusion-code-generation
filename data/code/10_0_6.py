import sys

def calculate_average(temp1: float | None = None, temp2: float | None = None) -> float:
    """
    Calculates the average of two temperature values with robust error handling.

    Args:
        temp1 (float): The first temperature value. Defaults to None if not provided via arguments.
        temp2 (float): The second temperature value. Defaults to None if not provided via arguments.

    Returns:
        float: The average of the two temperatures, or 0.0 if both are missing/invalid.
    
    Raises:
        ValueError: If either input is non-numeric when passed as a string argument.
    """
    # Handle cases where values might be strings that need conversion (simulating user input scenarios)
    def safe_parse(value):
        try:
            return float(value) if value is not None else 0.0
        except ValueError:
            raise ValueError(f"Invalid temperature format for {value}: expected a number.")

    # If arguments are provided as strings (simulating command line or input), parse them safely
    parsed_temp1 = safe_parse(temp1) if temp1 is not None and isinstance(temp1, str) else (temp1 if temp1 is not None else 0.0)
    parsed_temp2 = safe_parse(temp2) if temp2 is not None and isinstance(temp2, str) else (temp2 if temp2 is not None else 0.0)

    # Ensure we have valid numeric values to calculate the average
    if parsed_temp1 == 0.0 and parsed_temp2 == 0.0:
        return 0.0
    
    avg = (parsed_temp1 + parsed_temp2) / 2
    return avg

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    SAMPLE_TEMP_1 = "98.6"
    SAMPLE_TEMP_2 = "103.5"

    try:
        result = calculate_average(SAMPLE_TEMP_1, SAMPLE_TEMP_2)
        print(f"The average of {SAMPLE_TEMP_1} and {SAMPLE_TEMP_2} is {result:.2f}")
        
        # Additional test case for error handling simulation (non-numeric input)
        try:
            invalid_result = calculate_average("abc", "98.6")
        except ValueError as e:
            print(f"Error detected during calculation: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)