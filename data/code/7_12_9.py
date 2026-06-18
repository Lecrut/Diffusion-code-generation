def convert_time(value, from_unit, to_unit):
    """
    Converts a time value from one unit to another using seconds as an intermediate base.
    
    Supported units: 'seconds', 'minutes', 'hours', 'days', 'weeks'
    
    Args:
        value (float or int): The numeric value of the time period.
        from_unit (str): Source time unit ('seconds', 'minutes', 'hours', 'days', 'weeks').
        to_unit (str): Target time unit ('seconds', 'minutes', 'hours', 'days', 'weeks').
        
    Returns:
        float: The converted value in the target unit.
    
    Raises:
        ValueError: If an unsupported unit is provided or if from/to units are invalid strings.
    """
    # Define conversion factors to seconds (base unit)
    base_units = {
        'seconds': 1,
        'minutes': 60,
        'hours': 3600,
        'days': 86400,
        'weeks': 604800
    }

    # Validate input units against supported list
    valid_units = set(base_units.keys())
    
    if from_unit not in valid_units or to_unit not in valid_units:
        raise ValueError(f"Unsupported unit. Supported units are {valid_units}")

    try:
        val_float = float(value)
    except (TypeError, ValueError):
        raise TypeError("Value must be a number.")

    # Convert from source unit to seconds first
    value_in_seconds = val_float * base_units[from_unit]
    
    # Then convert from seconds to target unit
    return value_in_seconds / base_units[to_unit]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    test_cases = [
        (100, 'seconds', 'minutes'),
        (3.5, 'hours', 'days'),
        (720, 'minutes', 'hours'),
        (14, 'days', 'weeks'),
        (86400, 'seconds', 'hours'),
        (2 * 60 + 30, 'minutes', 'seconds') # 1 hour 30 minutes to seconds
    ]

    print("Time Conversion Results:")
    for val, frm, tgt in test_cases:
        result = convert_time(val, frm, tgt)
        print(f"{val} {frm} -> {result:.2f} {tgt}")