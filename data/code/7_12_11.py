def convert_time(value, from_unit, to_unit):
    """
    Converts a given time value from one unit to another using seconds as an intermediate base.
    
    Supported units: 'days', 'hours', 'minutes', 'seconds'.
    
    Parameters:
        value (float or int): The numerical value of the time duration.
        from_unit (str): Source time unit ('days', 'hours', 'minutes', 'seconds').
        to_unit (str): Target time unit ('days', 'hours', 'minutes', 'seconds').
        
    Returns:
        float: Converted time value in the target unit, rounded to 6 decimal places.
    
    Raises:
        ValueError: If unsupported units are provided or if input types are incorrect.
    
    Algorithm:
        1. Define conversion factors relative to seconds for each supported unit.
           - days   -> seconds: *86400
           - hours  -> seconds: *3600
           - minutes-> seconds: *60
           - seconds-> seconds: *1 (identity)
        2. Convert input value from source unit to seconds by multiplying with the factor for 'from_unit'.
        3. Divide the resulting seconds by the conversion factor of 'to_unit' to get target units.

    """
    
    # Map each time unit to its equivalent in seconds (multiplier)
    multipliers = {
        "days":   86400,      # 24 * 60 * 60
        "hours":  3600,       # 60 * 60
        "minutes":60,          # 60
        "seconds":1           # base unit
    }

    valid_units = set(multipliers.keys())

    if not isinstance(value, (int, float)):
        raise TypeError(f"Value must be a number, got {type(value).__name__}")

    from_lower = from_unit.lower()
    to_lower = to_unit.lower()

    if from_lower not in valid_units or to_lower not in valid_units:
        raise ValueError("Unsupported unit. Supported units are: days, hours, minutes, seconds.")

    factor_from = multipliers[from_lower]
    factor_to   = multipliers[to_lower]

    # Step 1: Convert source value to seconds (intermediate base)
    seconds_value = value * factor_from
    
    # Step 2: Convert seconds to target unit
    converted_seconds = seconds_value / factor_to

    return round(converted_seconds, 6)

if __name__ == "__main__":
    # Hard-coded sample values for testing without external input or files.
    
    test_cases = [
        {"value": 100, "from_unit": "hours", "to_unit": "days"},      # 1 day = 24 hours; result ~4 days (rounded)
        {"value": 365 * 86400 + 7200, "from_unit": "seconds", "to_unit": "years"}, 
    ]

    for i, case in enumerate(test_cases):
        try:
            res = convert_time(
                value=case["value"],
                from_unit=case["from_unit"].lower(),
                to_unit=case["to_unit"].lower()
            )
            print(f"Test {i + 1}:")
            print(f"Input ({case['value']}) in {case['from_unit']} -> Output: {res} in {case['to_unit']}")
        except Exception as e:
            print(f"Error in test case {i + 1}: {e}")

    # Additional manual calls to ensure comprehensive coverage of supported units.
    
    print("\n--- Manual Verification ---\n")

    result_1 = convert_time(5, "seconds", "minutes")
    print("Convert 5 seconds to minutes:", round(result_1)) # Expected: ~0.083...

    result_2 = convert_time(60 * 720, "hours", "days")
    print("Convert (4 days) in hours back to days:", round(result_2)) # Should be exactly or near 4
    
    try:
        bad_result = convert_time(-15, "invalid_unit", "minutes")
        print(f"Unexpected success for invalid unit: {bad_result}")
    except ValueError as ve:
        print("Correctly raised error for 'invalid' input:", str(ve))