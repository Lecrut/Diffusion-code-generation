import math

def convert_time(time_value: float, source_unit: str) -> dict:
    """
    Converts a given time value from one unit to another (seconds, minutes, hours).
    
    Args:
        time_value (float): The numeric value of the time.
        source_unit (str): The current unit ('seconds', 'minutes', or 'hours').
        
    Returns:
        dict: A dictionary containing values for seconds, minutes, and hours 
              based on the input converted across all three units.
    
    Raises:
        ValueError: If source_unit is not one of the supported units.
        TypeError: If time_value is not a number or source_unit is invalid type.
    """
    if not isinstance(time_value, (int, float)):
        raise TypeError("time_value must be an integer or float.")
    
    valid_units = {'seconds', 'minutes', 'hours'}
    if source_unit not in valid_units:
        raise ValueError(f"source_unit must be one of {valid_units}.")

    # Define conversion factors to a common base (seconds)
    seconds_value = time_value
    
    if source_unit == 'seconds':
        minutes_value = seconds_value / 60.0
        hours_value = seconds_value / 3600.0
    elif source_unit == 'minutes':
        # Convert input to seconds first, then calculate others for consistency across all fields
        seconds_value = time_value * 60.0
        minutes_value = time_value
        hours_value = (time_value * 60.0) / 3600.0
    elif source_unit == 'hours':
        # Convert input to seconds first, then calculate others for consistency across all fields
        seconds_value = time_value * 3600.0
        minutes_value = (time_value * 3600.0) / 60.0
        hours_value = time_value
    
    return {
        'seconds': round(seconds_value, 2),
        'minutes': round(minutes_value, 2),
        'hours': round(hours_value, 4)
    }

if __name__ == '__main__':
    # Sample test cases running without user input or external dependencies
    
    result_1 = convert_time(90.5, "seconds")
    print(f"Input: {result_1['minutes']} minutes and {result_1['hours']} hours.")

    result_2 = convert_time(3.75, "minutes")
    print(f"Input seconds equivalent to 3.75 mins is {round(result_2['seconds'], 4)}s")

    result_3 = convert_time(0.5, "hours")
    print(f"Input: {result_3['minutes']} minutes and {result_3['seconds']} seconds.")