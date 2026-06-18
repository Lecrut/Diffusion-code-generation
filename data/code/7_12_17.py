import re

def convert_time(value, from_unit, to_unit):
    """
    Converts a given time value between various units using seconds as an intermediate base unit.
    
    Supported units: 's', 'sec', 'second' (seconds)
                   'min', 'm', 'minute' (minutes)
                   'h', 'hr', 'hour' (hours)
                   'd', 'day' (days)
    
    The conversion process involves first converting the input to seconds, 
    and then from seconds to the target unit. All inputs are converted to float for calculation precision.
    
    Parameters:
        value (int or float): Time value in the specified source unit.
        from_unit (str): Source time unit string.
        to_unit (str): Destination time unit string.
        
    Returns:
        float: The converted time value in the destination unit.
                
    Raises:
        ValueError: If an unsupported unit is provided or conversion factor is invalid.
    
    Examples:
        >>> convert_time(1, 'h', 'min')
        60.0
        >>> convert_time('3 hours ', 'hr', 'sec')
        10800.0
    """

    # Unit mapping to seconds (conversion factor)
    units_to_seconds = {
        's': 1, 'sec': 1, 'second': 1,
        'min': 60, 'm': 60, 'minute': 60,
        'h': 3600, 'hr': 3600, 'hour': 3600,
        'd': 86400, 'day': 86400
    }

    # Normalize input strings for comparison (lowercase) and handle whitespace
    from_unit_str = re.sub(r'\s+', '', str(from_unit)).strip().lower()
    to_unit_str = re.sub(r'\s+', '', str(to_unit)).strip().lower()

    if from_unit_str not in units_to_seconds:
        raise ValueError(f"Unsupported source unit '{from_unit}'. Supported units are: {', '.join(units_to_seconds.keys())}")
    
    if to_unit_str not in units_to_seconds:
        raise ValueError(f"Unsupported target unit '{to_unit}'. Supported units are: {', '.join(units_to_units.keys())}")

    # Convert value to float and calculate seconds first, then convert to the desired unit
    try:
        val_float = float(value)
    except (ValueError, TypeError):
        raise ValueError(f"Invalid numeric input '{value}'")

    # 1. Value -> Seconds
    seconds_value = val_float * units_to_seconds[from_unit_str]

    # 2. Seconds -> Target Unit
    converted_time = seconds_value / units_to_seconds[to_unit_str]

    return float(converted_time)

if __name__ == '__main__':
    # Hard-coded sample values ensuring no external input or dependencies
    test_cases = [
        (1, 'h', 'min'),
        ('3 hours ', 'hr', 'sec'),
        (60, 'm', 'd'),
        (7200, 's', 'h'),
        (45, 'minute', 'hour')
    ]

    # Run tests and print results directly to stdout without user interaction
    for val_str, f_unit, t_unit in test_cases:
        result = convert_time(val_str, f_unit, t_unit)
        source_val_type = type(val_str).__name__
        output_msg = f"Converted {source_val_type} '{val_str}' [{f_unit}] -> [t_{t_unit}]: {result}"
        print(output_msg)