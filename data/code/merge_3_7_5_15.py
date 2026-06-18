def convert_to_appropriate_unit(total_seconds: int) -> tuple[int, str]:
    """
    Converts a total number of seconds into the most appropriate time unit.
    
    Returns a tuple (value_in_units, unit_name).
    
    Logic:
    - If >= 3600 seconds, convert to hours.
    - Else if >= 60 seconds, convert to minutes.
    - Otherwise, return in seconds.
    """
    if total_seconds >= 3600:
        value = total_seconds // 3600
        unit_name = "hours"
    elif total_seconds >= 60:
        value = total_seconds // 60
        unit_name = "minutes"
    else:
        value = total_seconds
        unit_name = "seconds"
    
    return value, unit_name

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input.
    samples = [86400, 3700, 125, 45]

    for sec in samples:
        converted_value, unit_name = convert_to_appropriate_unit(sec)
        print(f"{sec} seconds is equivalent to {converted_value} {unit_name}.")