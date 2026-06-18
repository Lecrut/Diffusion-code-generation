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
        ValueError: If unsupported units are provided or if from/to units match.
    """
    # Define conversion factors relative to seconds
    base_units = {
        'days': 86400,
        'hours': 3600,
        'minutes': 60,
        'seconds': 1
    }

    if from_unit not in base_units or to_unit not in base_units:
        raise ValueError(f"Unsupported unit. Supported units are {list(base_units.keys())}.")
    
    if from_unit == to_unit:
        return round(value, 6)

    # Convert source value to seconds (intermediate calculation)
    seconds = value * base_units[from_unit]
    
    # Convert seconds to target unit
    converted_value = seconds / base_units[to_unit]
    
    return round(converted_value, 6)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    
    test_cases = [
        (1.5, 'hours', 'minutes'),      # Expected: 90.0
        (24, 'days', 'seconds'),       # Expected: 2073600.0
        (0.25, 'hours', 'days'),       # Expected: 0.010417... -> rounded to 0.010417
        (90, 'minutes', 'seconds'),    # Expected: 5400.0
        (3600, 'seconds', 'hours'),    # Expected: 1.0
        (-2, 'days', 'hours')          # Negative value test -> -48.0
    ]

    for val, f_u, t_u in test_cases:
        result = convert_time(val, f_u, t_u)
        print(f"Converting {val} {f_u} to {t_u}: {result}")