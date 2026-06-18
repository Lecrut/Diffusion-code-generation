import math

def convert_time(value, from_unit, to_unit):
    """
    Converts a given time value from one unit to another using seconds as the base.
    
    Supported units: 'days', 'hours', 'minutes', 'seconds'.
    
    Args:
        value (float or int): The time value to convert.
        from_unit (str): Source unit of time ('days', 'hours', 'minutes', 'seconds').
        to_unit (str): Target unit of time ('days', 'hours', 'minutes', 'seconds').
        
    Returns:
        float: Converted time value in the target unit.
        
    Raises:
        ValueError: If units are not supported or input is invalid.
    """
    
    # Define conversion factors to seconds
    SECONDS_PER_UNIT = {
        'days': 86400,      # 24 * 60 * 60
        'hours': 3600,      # 60 * 60
        'minutes': 60,       # seconds in a minute
        'seconds': 1         # base unit
    }

    if from_unit not in SECONDS_PER_UNIT or to_unit not in SECONDS_PER_UNIT:
        raise ValueError(f"Unsupported units. Supported: {list(SECONDS_PER_UNIT.keys())}")
    
    try:
        value = float(value)
    except (TypeError, ValueError):
        raise TypeError("Input 'value' must be a number.")

    # Convert to seconds first
    seconds_in_source = SECONDS_PER_UNIT[from_unit] * value
    
    # Then convert from seconds to target unit
    seconds_per_target = SECONDS_PER_UNIT[to_unit]
    
    if seconds_per_target == 0:
        raise ValueError("Cannot divide by zero.")

    result_value = seconds_in_source / seconds_per_target
    
    return result_value

if __name__ == '__main__':
    pass
