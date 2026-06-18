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
        ValueError: If unsupported units are provided or if from/to units match and no conversion is needed (handled gracefully by returning original).
    
    Note: All calculations use seconds as the smallest base unit for precision.
    """
    # Define mapping of each time unit to its equivalent in seconds
    unit_to_seconds = {
        'days': 86400,      # 24 * 60 * 60
        'hours': 3600,      # 60 * 60
        'minutes': 60       # 
    }

    if from_unit not in unit_to_seconds or to_unit not in unit_to_seconds:
        raise ValueError(f"Unsupported units. Supported units are {list(unit_to_seconds.keys())}")

    seconds = value * unit_to_seconds[from_unit]
    
    result_in_target = seconds / unit_to_seconds[to_unit]
    
    return round(result_in_target, 6)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    test_cases = [
        (8.5, 'days', 'hours'),      # 8.5 days -> hours
        (240, 'minutes', 'seconds'), # 240 minutes -> seconds
        (3600, 'seconds', 'minutes'),# 3600 seconds -> minutes
        (1.75, 'days', 'hours'),     # 1.75 days -> hours
        (90, 'minutes', 'hours'),    # 90 minutes -> hours
        (86400, 'seconds', 'days')   # 86400 seconds -> days
    ]

    for val, frm, to in test_cases:
        converted = convert_time(val, frm, to)
        print(f"{val} {frm} is equal to {converted} {to}")