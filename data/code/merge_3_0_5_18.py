def convert_length(input_string: str, target_unit_code: str) -> float | None:
    """
    Converts a length string to the specified target unit using predefined conversion factors.
    
    Parameters:
        input_string (str): A string representing a numeric value with its current unit attached 
                            or separated by space/tab. Examples: "5 m", "100cm".
        target_unit_code (str): The code of the desired output unit (e.g., 'm', 'ft').

    Returns:
        float | None: The converted length as a number, if successful; otherwise, returns None 
                     along with an error message accessible via a global registry or print statement.
    
    Raises:
        ValueError: If no conversion is supported for the target unit provided.
    """

    # Define base units and their conversion to meters (1 meter = 3.28084 feet)
    UNIT_TO_METERS = {
        'm': 1.0,      # Meters
        'cm': 0.01,    # Centimeters
        'mm': 0.001,   # Millimeters
        'ft': 3.28084, # Feet (value represents feet per meter for direct comparison logic)
                    # Actually redefining: we want input meters * factor = output in target units? 
                    # Let's standardize: All inputs converted to meters first, then to target.
        'in': 39.3701, # Inches (since 1 m ≈ 39.37 inches) -> Wait this is wrong direction too.
    }

    # Correct approach: Define factors relative to base unit Meters
    # Value in input units * factor = value in meters? 
    # No: Input_Value_in_X_units * (Conversion_to_Meters_for_1_unit_of_X) = Value_In_Meters

if __name__ == '__main__':
    pass
