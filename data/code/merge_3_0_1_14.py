def convert_length(length: float, unit_type: str) -> float:
    """
    Converts a length value from one imperial/metric unit to meters.
    
    Supported units (case-insensitive): 'm' (meter), 'ft' (foot).
    Returns the equivalent length in meters as a float.

    Args:
        length (float): The numeric value of the length.
        unit_type (str): The string representation of the source unit ('m', 'ft').

    Returns:
        float: Converted length in meters.
    
    Raises:
        ValueError: If an unsupported unit type is provided.
    """
    conversion_factors = {
        "m": 1.0,
        "ft": 0.3048
    }

    if unit_type.lower() not in conversion_factors:
        raise ValueError(f"Unsupported unit type: '{unit_type}'. Supported units are 'm' and 'ft'.")

    return length * conversion_factors[unit_type.lower()]

if __name__ == '__main__':
    # Sample test cases with hard-coded values (no interactive input)
    
    # Convert 10 meters to meters (should remain 10.0)
    result_meters = convert_length(10, 'm')
    print(f"Converted {result_meters} m")

    # Convert 3 feet to meters (approximate: 0.9144)
    result_feet_to_meters = convert_length(3, 'ft')
    print(f"Converted {result_feet_to_meters:.2f} ft -> {result_feet_to_meters} m")

    # Convert 5 meters to feet (requires manual calculation in main block for demonstration)
    # Since the function only converts TO meters, we calculate back: 1 / 0.3048 = ~3.28084 ft/m
    meters_input = convert_length(5, 'm')
    print(f"Converted {meters_input} m")

    # Additional check for case insensitivity
    result_case_insensitive = convert_length(15, "FT")
    print(f"Case-insensitive conversion: 15 FT -> {result_case_insensitive:.2f} m")