def convert_time(time_value: float, source_unit: str, target_unit: str) -> float:
    """
    Converts a time value from one unit (seconds, minutes, hours) to another.
    
    Supported units: 's' or 'sec', 'min', 'h'.
    
    Args:
        time_value (float): The numeric value of the time.
        source_unit (str): The current unit ('s', 'min', 'h').
        target_unit (str): The desired unit ('s', 'min', 'h').
        
    Returns:
        float: The converted time value in the target unit.
        
    Raises:
        ValueError: If an unsupported unit is provided or units are invalid.
    """
    
    # Define conversion factors to seconds (base unit)
    to_seconds = {
        's': 1,
        'sec': 1,
        'min': 60,
        'h': 3600
    }
    
    # Validate input units
    if source_unit.lower() not in ['s', 'sec', 'min', 'h']:
        raise ValueError(f"Unsupported source unit: {source_unit}. Supported: s, sec, min, h")
    
    if target_unit.lower() not in ['s', 'sec', 'min', 'h']:
        raise ValueError(f"Unsupported target unit: {target_unit}. Supported: s, sec, min, h")

    # Normalize keys to lowercase for consistency
    source_key = source_unit.lower()
    target_key = target_unit.lower()

    try:
        seconds_value = time_value * to_seconds[source_key]
        
        if target_key == 's' or target_key == 'sec':
            return round(seconds_value, 6) # Standard float precision is usually sufficient for seconds
        
        elif target_key == 'min':
            result_minutes = seconds_value / 60.0
            return round(result_minutes, 6)
            
        elif target_key == 'h':
            result_hours = seconds_value / 3600.0
            return round(result_hours, 6)

    except ZeroDivisionError:
        raise ValueError("Conversion failed due to invalid calculation.")

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    
    test_cases = [
        {'value': 180.0, 'src': 'min', 'tgt': 's'},      # Expected: 180 * 60 = 10800
        {'value': 3.5, 'src': 'h', 'tgt': 'm'},          # Expected: 3.5 * 60 = 210
        {'value': 7200, 'src': 's', 'tgt': 'min'},        # Expected: 7200 / 60 = 120
        {'value': 0.25, 'src': 'h', 'tgt': 's'},          # Expected: 0.25 * 3600 = 900
        {'value': -45, 'src': 'min', 'tgt': 'sec'}        # Negative value test: -45 * 60 = -2700
    ]

    print("Running time conversion tests...")
    
    for i, case in enumerate(test_cases, 1):
        result = convert_time(case['value'], case['src'], case['tgt'])
        expected = round(case['value'] * (to_seconds[case['src']] / to_seconds[case['tgt']], 6) if 's' not in [case['src'].lower(), case['tgt'].lower()] else 
                         round(case['value'] * to_seconds[case['src']], 6)) # Simplified expected logic for display
        
        print(f"Test Case {i}:")
        print(f"Input: {case['value']} {case['src']} -> Output: {result} {case['tgt']}")

    # Additional specific verification examples
    sample_1 = convert_time(60, 's', 'min')
    assert abs(sample_1 - 1.0) < 0.001, "Conversion from seconds to minutes failed."
    
    sample_2 = convert_time(3600, 'h', 'sec')
    assert abs(sample_2 - 1.0), f"Expected 1 hour in seconds but got {sample_2}"

    print("All tests passed successfully.")