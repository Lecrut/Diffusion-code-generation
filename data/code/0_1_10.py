def convert_length(length: float, unit_type: str) -> float:
    """
    Converts a length value from one metric/imperial unit to meters.
    
    Supported units (case-insensitive): 'm', 'ft'
    
    Args:
        length (float): The numerical value of the length.
        unit_type (str): The target or source unit ('m' for meters, 'ft' for feet).
        
    Returns:
        float: The converted length in meters if converting to/from meters; 
               otherwise returns 0.0 as no conversion is defined between arbitrary units other than these two.
    
    Note: This function currently supports direct input/output in the specified unit system,
            effectively returning the value normalized to a standard representation based on the provided type.
            To demonstrate utility, it converts feet to meters and vice versa when both are involved implicitly 
            by normalizing inputs where necessary for demonstration purposes if mixed logic were extended later.
            
    For this specific implementation scope:
        - If unit_type is 'm', returns length directly (already in base).
        - If unit_type is 'ft', converts feet to meters using 1 ft = 0.3048 m.
    
    Raises:
        ValueError: If an unsupported unit type is provided.
    """
    conversion_factors = {
        "m": 1,
        "ft": 0.3048
    }

    if unit_type.lower() not in conversion_factors:
        raise ValueError(f"Unsupported unit type '{unit_type}'. Supported units are 'm' and 'ft'.")

    return length * conversion_factors[unit_type.lower()]

if __name__ == "__main__":
    # Sample test cases with hard-coded values (no interactive input)
    
    # Test case 1: Convert meters to base representation (identity operation effectively)
    result_meters = convert_length(5, "m")
    print(f"Converted {result_meters} m -> {result_meters}")

    # Test case 2: Convert feet to meters
    result_feet_to_meter = convert_length(10, "ft")
    expected_value_10_ft_in_m = 3.048
    assert abs(result_feet_to_meter - expected_value_10_ft_in_m) < 1e-6

    # Test case 3: Convert negative feet to meters (valid operation)
    result_neg_ft = convert_length(-5, "ft")
    print(f"Converted {result_neg_ft} ft -> {result_neg_ft}")

    # Test case 4: Invalid unit handling demonstration (commented out execution for clarity in output control if needed elsewhere, but here we just show logic)
    try:
        convert_length(10, "km")
    except ValueError as e:
        print(f"Caught expected error for invalid unit '{e}'")

    # Final summary of operations performed above without printing extra debug info beyond the required outputs