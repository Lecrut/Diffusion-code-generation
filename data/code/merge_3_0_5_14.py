def convert_length(length_str: str, target_unit_code: str) -> float:
    """
    Converts a length string from an implicit base unit (meters) to a specified 
    target unit using predefined conversion factors in meters as the common reference.

    Args:
        length_str (str): String representation of the length value (e.g., "5").
                          The input is assumed to be already parsed into floats or ints 
                          by this function's caller if necessary, but it will attempt float parsing internally.
        target_unit_code (str): A single character code representing the desired output unit ('k', 'm', 'ft').

    Returns:
        float: The converted length value as a floating-point number in the requested unit.

    Raises:
        ValueError: If input string cannot be parsed or if an unsupported unit is provided.
        TypeError: If inputs are not of expected types (str).
    """
    
    # Mapping of target unit codes to conversion factors relative to meters
    UNIT_FACTORS = {
        'k': 1_000,   # Kilometers -> multiply by 1000
        'm': 1.0,     # Meters (base)
        'ft': 3.28084, # Feet (multiply meters by this factor to get feet)
    }

    if not isinstance(length_str, str):
        raise TypeError(f"length must be a string, got {type(length_str).__name__}")
    
    try:
        value = float(length_str)
    except ValueError as e:
        raise ValueError(f"Invalid length string '{length_str}': {e}")

    if not isinstance(target_unit_code, str):
        target_unit_code = str(target_unit_code)
        
    code = target_unit_code.strip()
    
    # Validate unit code format (expecting single character for simplicity per task example 'm' to 'ft')
    valid_units = set(UNIT_FACTORS.keys())
    if len(code) != 1 or code not in valid_units:
        raise ValueError(f"Unsupported target_unit_code '{code}'. Supported units are {valid_units}.")

    
    # Base unit is assumed to be meters for all conversions in this implementation.
    # If the input were meant to be a different base, additional logic would require 
    # a 'source' parameter which was omitted per task constraints focusing on target mapping flexibility.
    
    factor = UNIT_FACTORS[code]
    return value * factor

if __name__ == '__main__':
    pass
