def convert_length(length_str, target_unit):
    """
    Converts a length string from various units to the specified target unit.
    
    Supported input units: m (meters), ft (feet), in (inches).
    Target units: meters ('m'), feet ('ft').
    
    Args:
        length_str (str): String representing a numeric value and optionally its current unit.
                          Format can be "123" or "123 m". If no unit is provided, assumed to be 'm'.
        target_unit (str): The desired output unit code ('m' for meters, 'ft' for feet).
        
    Returns:
        float: The converted length value.
        
    Raises:
        ValueError: If the input string cannot be parsed or if an unsupported unit is encountered.
    
    Dictionary mapping used internally for flexibility and extensibility logic simulation 
    (though direct math constants are applied here based on standard definitions).
    """
    # Standard conversion factors relative to meters
    unit_factors = {
        'm': 1,
        'ft': 0.3048,   # 1 foot in meters
        'in': 0.0254     # 1 inch in meters
    }
    
    try:
        value_str, current_unit_str = length_str.strip().split()
        
        if not all(part.isdigit() for part in [value_str]):
            raise ValueError("Length string must contain a valid numeric value.")
            
        value = float(value_str)
        
        # If no unit is specified after the number, assume meters (standard SI base)
        if current_unit_str.lower() == '':
            current_unit_code = 'm'
        else:
            current_unit_code = current_unit_str.strip().lower()
            
    except ValueError as e:
        raise ValueError(f"Invalid length string format. Expected numeric value with optional unit (e.g., '10 m').") from e
    
    if target_unit.lower() not in ['m', 'ft']:
        raise ValueError("Target unit must be either 'm' or 'ft'.")
    
    # Ensure current input unit is supported for conversion base calculation
    if current_unit_code not in unit_factors:
        raise ValueError(f"Unsupported input unit code: {current_unit_str}. Supported units are m, ft.")

    try:
        converted_meters = value * unit_factors[current_unit_code]
        
        if target_unit.lower() == 'm':
            return float(converted_meters) # Return as integer-like float or just the number
        else:
            return float(converted_meters / 0.3048) 
    except ZeroDivisionError:
        raise ValueError("Conversion failed due to invalid operation.")

if __name__ == '__main__':
    sample_inputs = [
        ("12 m", "ft"),
        ("5 ft", "m"),
        ("60 in", "ft"),
        ("3.5", "m") # No unit suffix, assumes meters
    ]

    for length_str, target_unit in sample_inputs:
        try:
            result = convert_length(length_str, target_unit)
            print(f"Converted {length_str} to {target_unit}: {result}")
        except ValueError as ve:
            print(f"Error converting '{length_str}' to {target_unit}:", ve)