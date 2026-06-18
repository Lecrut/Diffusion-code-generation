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
        float: Converted time value in the target unit.
    
    Raises:
        ValueError: If unsupported units are provided or conversion is invalid.
    """
    # Define seconds equivalent for each supported unit
    to_seconds = {
        'days': 86400,
        'hours': 3600,
        'minutes': 60,
        'seconds': 1
    }

    if from_unit not in to_seconds or to_unit not in to_seconds:
        raise ValueError(f"Unsupported units. Supported: {list(to_seconds.keys())}")

    # Convert input value to seconds first (intermediate calculation)
    total_seconds = value * to_seconds[from_unit]

    # Then convert seconds to target unit
    result_value = total_seconds / to_seconds[to_unit]

    return float(result_value)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    # Sample 1: Convert 2 days to hours
    result_1 = convert_time(2, 'days', 'hours')
    
    # Sample 2: Convert 90 minutes to seconds
    result_2 = convert_time(90, 'minutes', 'seconds')
    
    # Sample 3: Convert 5 hours to days
    result_3 = convert_time(5, 'hours', 'days')
    
    # Sample 4: Convert 186400 seconds back to days (round trip check)
    round_trip_result = convert_time(convert_time(2, 'days', 'seconds'), 'seconds', 'days')

    print(f"Sample 1 - {result_1} hours")      # Expected: 48.0
    print(f"Sample 2 - {result_2} seconds")     # Expected: 5400.0
    print(f"Sample 3 - {result_3} days")       # Expected: ~0.216 (approx)
    print(f"Round trip check - {round_trip_result:.2f} days")   # Should be close to 2.0