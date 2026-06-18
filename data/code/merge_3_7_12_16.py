import math

def convert_time(value, from_unit, to_unit):
    """
    Converts a time value from one unit to another using seconds as an intermediate base unit.
    
    Args:
        value (float or int): The time value to be converted.
        from_unit (str): The source time unit ('day', 'hour', 'minute', 'second').
        to_unit (str): The target time unit ('day', 'hour', 'minute', 'second').
        
    Returns:
        float: The converted time value in the target unit, rounded to 6 decimal places.
            
    Raises:
        ValueError: If an unsupported unit is provided or if from_unit and to_unit are identical.
    
    Supported units: day, hour, minute, second
    
    Examples:
        >>> convert_time(100, 'second', 'minute')
        1.666667
        
        >>> convert_time(365, 'day', 'hour')
        8760.0
    """
    
    # Define conversion factors to seconds for each unit
    units_to_seconds = {
        'second': 1,
        'minute': 60,
        'hour': 3600,
        'day': 86400
    }

    if from_unit not in units_to_seconds:
        raise ValueError(f"Unsupported unit '{from_unit}'. Supported units are {list(units_to_seconds.keys())}")
    
    if to_unit not in units_to_seconds:
        raise ValueError(f"Unsupported unit '{to_unit}'. Supported units are {list(units_to_seconds.keys())}")

    # Validate that source and target units are different (though conversion logic handles same inputs too)
    # The problem implies converting between "any two specified", so if they are the same, return original value.
    
    seconds = value * units_to_seconds[from_unit]
    result_in_target = seconds / units_to_seconds[to_unit]

    return round(result_in_target, 6)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    test_cases = [
        (100, 'second', 'minute'),      # 100 seconds -> minutes
        (365, 'day', 'hour'),          # 365 days -> hours
        (90, 'minute', 'hour'),        # 90 minutes -> hours
        (7200, 'second', 'day'),       # 7200 seconds -> days
        (1.5, 'hour', 'minute'),       # 1.5 hours -> minutes
        (366.25, 'day', 'second')      # Leap day in seconds
    ]

    print("Time Conversion Results:")
    for value, from_u, to_u in test_cases:
        converted = convert_time(value, from_u, to_u)
        print(f"{value} {from_u} -> {converted:.6f} {to_u}")