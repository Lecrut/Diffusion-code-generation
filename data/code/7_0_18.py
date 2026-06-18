def convert_time(value: float, source_unit: str, target_unit: str) -> float:
    """
    Converts a time value from one unit to another among seconds, minutes, and hours.
    
    Args:
        value (float): The numerical value of the time.
        source_unit (str): The original unit ('seconds', 'minutes', or 'hours').
        target_unit (str): The desired unit for conversion.
        
    Returns:
        float: The converted time value in the target unit.
        
    Raises:
        ValueError: If input units are invalid or do not match expected format.
    
    Note:
        - Input values must be non-negative numbers representing absolute durations.
        - Case-insensitive string comparison for source_unit and target_unit is supported.
    """
    valid_units = {'seconds', 'minutes', 'hours'}
    
    if source_unit.lower() not in valid_units or target_unit.lower() not in valid_units:
        raise ValueError(f"Unsupported units provided. Valid options are {valid_units}")

    # Normalize input strings to lowercase for consistent processing
    src = source_unit.lower().strip()
    tgt = target_unit.lower().strip()

    if value < 0:
        raise ValueError("Time values must be non-negative.")

    # Conversion factors relative to seconds (base unit)
    conversion_to_seconds = {
        'seconds': lambda x, _: x,
        'minutes': lambda x, _: x * 60.0,
        'hours': lambda x, _: x * 3600.0
    }

    # Convert source value to seconds first (intermediate step)
    intermediate_seconds = conversion_to_seconds[src](value, None)

    if tgt == 'seconds':
        return intermediate_seconds
    
    elif tgt == 'minutes':
        return round(intermediate_seconds / 60.0, 10) # Using rounding for float precision stability
    
    else: # target is hours
        return round(intermediate_seconds / 3600.0, 10)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without external input
    test_cases = [
        {'value': 90, 'source_unit': 'seconds', 'target_unit': 'minutes'},
        {'value': 45.5, 'source_unit': 'minutes', 'target_unit': 'hours'},
        {'value': 2.75, 'source_unit': 'hours', 'target_unit': 'seconds'},
        {'value': 1800, 'source_unit': 'seconds', 'target_unit': 'hours'}, # Edge case: whole hours to seconds and back
    ]

    print("Time Conversion Demo")
    for i, test in enumerate(test_cases, 1):
        result = convert_time(
            value=test['value'], 
            source_unit=test['source_unit'], 
            target_unit=test['target_unit']
        )
        display_str = f"{test['value']} {test['source_unit'].capitalize()} " \
                      + "->" + f"{result:.2f} {test['target_unit'].capitalize()}"
        print(f"Test Case {i}: {display_str}")

    # Additional manual verification block for clarity
    manual_check = convert_time(1.5, 'hours', 'minutes')
    expected_manual = 90.0
    
    if abs(manual_check - expected_manual) < 1e-6:
        print(f"\nVerification passed: {manual_check} minutes is correct.")
    else:
        print("\nVerification failed!")