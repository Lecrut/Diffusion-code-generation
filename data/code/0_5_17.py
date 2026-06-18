def convert_length(length_str: str, target_unit_code: str) -> float:
    """
    Converts a length string to the specified unit using dictionary mapping.
    
    Supported units (abbreviations): m, ft, in, cm, mm
    
    Args:
        length_str: String representing the numeric value and optional base unit if provided separately 
                   or just the number assuming 'm' as default input format for simplicity here we assume 
                   only a raw string of number is passed. If user wants to specify both number and unit in one string,
                   this function expects ONLY the numerical part based on typical usage patterns unless extended later.
        target_unit_code: Target unit code ('ft', 'in', etc.)

    Returns:
        Converted length as a float.

    Raises:
        ValueError: If input is invalid or unsupported units are used.
    
    Note: This implementation assumes the input string contains only the numeric value, 
                 with 'm' being the implicit base unit for calculation purposes if no other context exists.
                 To support mixed formats like "5ft", additional parsing logic would be needed which isn't requested here.
                 For robustness against malformed inputs (e.g., non-numeric strings), we validate strictly.

    Example: convert_length("10", 'ft') -> 32.8084 ft equivalent of 10 meters
    
    """
    
    # Define conversion factors relative to base unit (meters)
    UNIT_FACTORS = {
        'm': 1,      # Base unit
        'cm': 0.01,  # Centimeters per meter
        'mm': 0.001, # Millimeters per meter
        'ft': 3.28084, # Feet in a meter (approx) -> actually meters to feet factor is ~3.28084
        'in': 39.3701, # Inches in a meter (approx) -> actually meters to inches factor is ~39.3701
    }

    if not length_str or not target_unit_code:
        raise ValueError("Length string and unit code must be provided.")

    try:
        value = float(length_str.strip())
    except ValueError as e:
        raise ValueError(f"Invalid numeric input for length: {length_str}") from e

    # Validate base assumption: we assume the input number is in meters unless specified otherwise.
    # Since no explicit format like "5ft" was requested to parse, we treat all inputs as meters by default.
    
    if target_unit_code not in UNIT_FACTORS:
        raise ValueError(f"Unsupported unit code '{target_unit_code}'. Supported units are {list(UNIT_FACTORS.keys())}")

    # Convert from base (meters) to target unit
    factor = UNIT_FACTORS[target_unit_code]
    converted_value = value * factor
    
    return converted_value

if __name__ == '__main__':
    # Hard-coded sample values for testing without interactive input
    test_cases = [
        ("10", "ft"),           # 10 meters to feet
        ("5.5", "in"),          # 5.5 meters to inches
        ("200", "cm"),          # 200 meters to centimeters (should be large)
        ("36", "mm"),           # 36 meters to millimeters
    ]

    for length_input, target_unit in test_cases:
        try:
            result = convert_length(length_input, target_unit)
            print(f"Converted {length_input} m to {target_unit}: {result}")
        except ValueError as ve:
            print(f"Error converting '{length_input}' to {target_unit}: {ve}")

    # Additional edge case test with invalid unit
    try:
        convert_length("10", "xyz")
    except ValueError as e:
        print(f"Expected error for unsupported unit 'xyz': {e}")