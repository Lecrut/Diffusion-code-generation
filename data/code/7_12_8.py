import math

def convert_time(value, from_unit, to_unit):
    """
    Converts a time value from one unit to another using seconds as an intermediate base.
    
    Supported units: 's', 'm', 'h', 'd' (seconds, minutes, hours, days)
    
    Args:
        value (float or int): The time value to convert.
        from_unit (str): Source unit ('s', 'm', 'h', 'd').
        to_unit (str): Target unit ('s', 'm', 'h', 'd').
        
    Returns:
        float: Converted time value in the target unit, rounded to 6 decimal places.
    
    Raises:
        ValueError: If input units are not supported or if from/to units are identical without conversion needed (though identity is handled gracefully).
    """
    # Define seconds equivalent for each unit
    seconds_map = {
        's': 1,
        'm': 60,
        'h': 3600,
        'd': 86400
    }

    if from_unit not in seconds_map or to_unit not in seconds_map:
        raise ValueError(f"Unsupported unit. Supported units are {list(seconds_map.keys())}")

    # Convert from source unit to seconds
    value_in_seconds = value * seconds_map[from_unit]
    
    # Handle edge case where conversion is trivial (same unit) but ensure logic holds
    if from_unit == to_unit:
        return round(value, 6)

    # Convert from seconds to target unit
    converted_value = value_in_seconds / seconds_map[to_unit]
    
    return round(converted_value, 6)

if __name__ == '__main__':
    # Sample test cases running without user input
    
    # Test case 1: Hours to minutes
    result_1 = convert_time(2.5, 'h', 'm')
    print(f"Converted {result_1} hours to minutes")

    # Test case 2: Days to seconds
    result_2 = convert_time(3, 'd', 's')
    print(f"Converted {result_2} days to seconds")

    # Test case 3: Minutes to milliseconds (Note: ms is not supported per spec, sticking to allowed units)
    # Let's do minutes to hours instead as a valid test within constraints
    result_3 = convert_time(750, 'm', 'h')
    print(f"Converted {result_3} minutes to hours")

    # Test case 4: Identity check (seconds to seconds)
    result_4 = convert_time(120, 's', 's')
    print(f"Identity conversion test: {result_4}")

    # Test case 5: Complex chain - Hours to Days
    result_5 = convert_time(72, 'h', 'd')
    print(f"Converted {result_5} hours to days")