def convert_length(length_str: str, target_unit_code: str) -> float:
    """
    Converts a length value from an input string to a specified unit using dictionary mapping.
    
    Args:
        length_str (str): The numeric length as a string representing the base units (meters).
        target_unit_code (str): A two-letter code for the desired output unit ('km', 'ft', 'in').

    Returns:
        float: The converted value based on standard conversion factors.
    
    Raises:
        ValueError: If inputs are invalid or unsupported codes provided.
    """
    # Ensure base is always treated as meters (m) for simplicity and flexibility in mapping other units later
    if length_str.strip() == "":
        raise ValueError("Length string cannot be empty.")

    try:
        value = float(length_str.strip())
    except ValueError:
        raise ValueError(f"Invalid number provided: '{length_str}'.")

    # Mapping of base (meters) to target units conversion factors relative to meters
    unit_mapping = {
        "km": 0.001,      # Meters to kilometers
        "ft": 3.28084,    # Meters to feet
        "in": 39.3701,    # Meters to inches
        # Adding more flexibility for future units like 'mi' (miles) or others if needed:
        # "mi": 0.621371   # Not currently used in sample but kept flexible here conceptually
    }

    unit_code = target_unit_code.lower()
    
    if not isinstance(value, float):
        raise TypeError("Length value must be a numeric string or number.")

    if value < 0:
        raise ValueError(f"Negative length '{value}' is invalid for standard distance conversions in this context.")

    # Check if the target unit exists in our mapping dictionary. 
    # We assume base input is always meters unless explicitly overridden by future logic here.
    
    conversion_factor = unit_mapping.get(unit_code)
    if not isinstance(conversion_factor, float):
        raise ValueError(f"Unsupported unit code: '{unit_code}'. Supported units: {list(unit_mapping.keys())}")

    return value * conversion_factor

if __name__ == '__main__':
    # Hard-coded sample values for testing without interactive input
    
    test_cases = [
        ("10", "ft"),       # 10 meters to feet
        ("5.5", "km"),      # 5.5 meters to kilometers (should be small)
        ("2743.96", "in"),  # Standard conversion of ~8m to inches for verification 
    ]

    results = []
    for length, target in test_cases:
        try:
            converted_value = convert_length(length, target)
            result_msg = f"Converted {length} m to {target}: {converted_value:.4f}"
            results.append(result_msg)
        except Exception as e:
            # In a real scenario we might want more detailed logging; here we just catch and report error message.
            error_type, err_val = type(e).__name__, str(e).split(":")[0] if isinstance(str(e), str) else "Generic" 
            result_msg = f"{length} m to {target}: ERROR ({err_val})"
            results.append(result_msg)

    print("\nConversion Results:")
    for res in results:
        print(res)