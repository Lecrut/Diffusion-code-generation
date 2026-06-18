def convert_length(length_str, target_unit_code):
    """
    Converts a length string to the specified unit using a dictionary mapping.
    
    Args:
        length_str (str): String representing the numeric value of the length in meters.
                          Expected format: "number" or "+/- number".
        target_unit_code (str): Target unit code ('m', 'ft'). Default is 'm'.
        
    Returns:
        float: Converted length as a float rounded to 2 decimal places.
        
    Raises:
        ValueError: If the input string cannot be parsed into a valid numeric value,
                   if target_unit_code is not supported, or if no conversion logic exists for given units.
    
    Supported Units: 'm' (meters), 'ft' (feet)
    Conversion Factors relative to meters: 1 ft = 0.3048 m
    
    Note: This function assumes the input string represents a magnitude in meters. 
          If negative values are needed, they should be provided as part of the numeric value.
    """
    
    # Dictionary mapping unit codes to their conversion factor relative to base (meters)
    UNIT_FACTORS = {
        'm': 1.0,
        'ft': 0.3048
    }

    if target_unit_code not in UNIT_FACTORS:
        raise ValueError(f"Unsupported target unit code: '{target_unit_code}'. Supported units are m and ft.")

    # Parse the input string to a float
    try:
        length_value = float(length_str)
    except (ValueError, TypeError):
        raise ValueError(f"Invalid numeric value provided for conversion. Input was: {length_str}")

    if target_unit_code == 'm':
        return round(length_value * UNIT_FACTORS['m'], 2)
    
    elif target_unit_code == 'ft':
        # Convert meters to feet by dividing the meter length by the factor (0.3048 m/ft)
        converted_length = length_value / UNIT_FACTORS['ft']
        return round(converted_length, 2)

def main():
    """Main execution block with hard-coded sample values."""
    
    # Sample inputs for testing different scenarios
    
    # Test case 1: Convert meters to feet (standard positive value)
    result_m_to_ft = convert_length("5.0", "ft")
    
    # Test case 2: Keep as meters (identity conversion logic applied via factor of 1.0)
    result_m_to_m = convert_length("-3.4", "m")
    
    # Test case 3: Attempting to use an unsupported unit should raise ValueError
    try:
        invalid_result = convert_length("2.5", "km")
    except ValueError as e:
        print(f"Caught expected error for unsupported unit: {e}")

    # Output results from valid conversions
    print(f"Meters (5.0) to Feet: {result_m_to_ft} ft")
    print(f"Meters (-3.4) to Meters: {result_m_to_m} m")

if __name__ == '__main__':
    main()