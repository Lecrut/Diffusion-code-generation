import time as _time_module

# Define all valid time units relative to seconds (base unit)
UNIT_TO_SECONDS = {
    'nanosecond': 1e-9,
    'microsecond': 1e-6,
    'millisecond': 1e-3,
    'second': 1.0,
    'minute': 60.0,
    'hour': 3600.0,
    'day': 86400.0,
}

def convert_time(value, from_unit, to_unit):
    """
    Converts a time value from one unit to another using seconds as the intermediate base.
    
    Args:
        value (float or int): The numeric value of the time duration.
        from_unit (str): Source time unit string (e.g., 'minute', 'hour').
        to_unit (str): Target time unit string (e.g., 'second', 'day').
        
    Returns:
        float: Converted time value in the target unit.
        
    Raises:
        ValueError: If input units are not recognized or if conversion is impossible between same types without scaling logic errors (handled by dict lookup).
        TypeError: If inputs are not numeric strings/numbers or units are invalid.
    """
    
    # Normalize input to lowercase for consistent lookups
    from_unit_lower = from_unit.lower()
    to_unit_lower = to_unit.lower()

    if from_unit_lower not in UNIT_TO_SECONDS or to_unit_lower not in UNIT_TO_SECONDS:
        raise ValueError(f"Unsupported time units. Valid units are {list(UNIT_TO_SECONDS.keys())}")
    
    seconds_value = value * UNIT_TO_SECONDS[from_unit_lower]
    converted_value = seconds_value / UNIT_TO_SECONDS[to_unit_lower]
    
    return float(converted_value)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    test_cases = [
        (3600, 'second', 'minute'),       # 1 hour -> minute
        (90, 'minute', 'hour'),           # 1.5 hours -> hour
        (86400, 'day', 'week'),           # Note: week not in base units list below, will adjust to valid set or extend logic
        
    ]

    # Extend UNIT_TO_SECONDS if needed for the sample block to work fully as per "any two specified" requirement.
    # However, strict adherence suggests only using defined ones unless extended explicitly. 
    # Let's add 'week' and 'year' to make samples more diverse while keeping logic robust.
    
    # Re-defining UNIT_TO_SECONDS with additional units for comprehensive testing in the main block context if needed,
    # but strictly following "any two specified" implies we should support them dynamically or pre-define them here.
    # To ensure the sample runs without error and covers diverse cases:
    
    FULL_UNIT_MAP = {
        'nanosecond': 1e-9,
        'microsecond': 1e-6,
        'millisecond': 1e-3,
        'second': 1.0,
        'minute': 60.0,
        'hour': 3600.0,
        'day': 86400.0,
        'week': 7 * 24 * 3600, # Added for sample completeness
        'month': 30 * 24 * 3600, # Approximation added for sample completeness (optional but helpful)
        'year': 365.25 * 24 * 3600, # Leap year average approximation
    }

    def convert_time_extended(value, from_unit, to_unit):
        f_u = from_unit.lower()
        t_u = to_unit.lower()
        
        if f_u not in FULL_UNIT_MAP or t_u not in FULL_UNIT_MAP:
            raise ValueError(f"Invalid units. Available: {list(FULL_UNIT_MAP.keys())}")
            
        secs = value * FULL_UNIT_MAP[f_u]
        return secs / FULL_UNIT_MAP[t_u]

    # Run specific test cases using the extended map to ensure samples work as intended in a standalone run
    print("Running time conversion tests...")
    
    sample_1 = convert_time_extended(3600, 'second', 'minute')
    assert abs(sample_1 - 1.0) < 1e-9
    
    sample_2 = convert_time_extended(86400, 'day', 'week')
    # Expected: 86400 / (7*86400) = 1/7 ≈ 0.142857...
    
    sample_3 = convert_time_extended(1, 'year', 'second')
    expected_sec_year = FULL_UNIT_MAP['year']
    assert abs(sample_3 - expected_sec_year) < 1e-6

    print(f"Test 1 (hour to minute): {sample_1}")
    print(f"Test 2 (day to week): {sample_2:.5f} weeks")
    print(f"Test 3 (year to second): {sample_3 / FULL_UNIT_MAP['second']:.0e} seconds")

    # Additional edge case: same unit conversion should return original value
    sample_same = convert_time_extended(10, 'hour', 'hour')
    assert abs(sample_same - 10) < 1e-9
    
    print("All tests passed successfully.")