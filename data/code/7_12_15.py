import math

def convert_time(value, from_unit, to_unit):
    """
    Converts a time value from one unit to another using seconds as an intermediate base.
    
    Supported units: 'days', 'hours', 'minutes', 'seconds'
    
    Args:
        value (float or int): The time value to convert.
        from_unit (str): Source unit ('days', 'hours', 'minutes', 'seconds').
        to_unit (str): Target unit ('days', 'hours', 'minutes', 'seconds').
        
    Returns:
        float: Converted time value in the target unit, rounded to 6 decimal places.
    
    Raises:
        ValueError: If unsupported units are provided or if from_unit equals to_unit without checking validity first.
    """
    # Define conversion factors relative to seconds (1 second = 1s)
    # days -> hours * 24; hours -> minutes * 60; etc.
    unit_factors_to_seconds = {
        'days': 86400,      # 24 * 60 * 60
        'hours': 3600,      # 60 * 60
        'minutes': 60,
        'seconds': 1
    }

    if from_unit not in unit_factors_to_seconds or to_unit not in unit_factors_to_seconds:
        raise ValueError(f"Unsupported units. Supported units are {list(unit_factors_to_seconds.keys())}")
    
    # Convert input value to seconds first (intermediate calculation)
    seconds = value * unit_factors_to_seconds[from_unit]

    # Then convert from seconds to target unit
    result_in_target = seconds / unit_factors_to_seconds[to_unit]

    return round(result_in_target, 6)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    test_cases = [
        (8.5, 'days', 'hours'),      # Expected: ~204 hours
        (1.75, 'hours', 'minutes'),  # Expected: 60 minutes
        (90, 'minutes', 'seconds'),  # Expected: 5400 seconds
        (3600, 'seconds', 'days'),   # Expected: ~0.041667 days
        (24 * 60 * 60, 'hours', 'days'), # Exact conversion test
    ]

    print("Time Conversion Results:")
    for val, frm, to in test_cases:
        converted = convert_time(val, frm, to)
        print(f"{val} {frm} -> {converted} {to}")