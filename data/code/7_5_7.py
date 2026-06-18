def format_duration(total_seconds: int) -> tuple[int | float, str]:
    """
    Convert a total number of seconds into the most appropriate time unit.
    
    Returns:
        A tuple containing (magnitude, unit_name).
        
    Logic:
        - If >= 3600, return hours (integers).
        - Else if >= 60, return minutes (floats with .1 precision for partial mins).
        - Otherwise, return seconds as an integer.
    """
    if total_seconds >= 3600:
        magnitude = int(total_seconds / 3600)
        unit_name = "hours"
    elif total_seconds >= 60:
        # Use round to nearest tenth for cleaner output on partial minutes/seconds within an hour context, 
        # though standard float division is sufficient here.
        magnitude = total_seconds / 60
        unit_name = "minutes"
    else:
        magnitude = int(total_seconds)
        unit_name = "seconds"
    
    return magnitude, unit_name

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input.
    samples = [86400, 9125, 3700]

    for sec in samples:
        duration_magnitude, duration_unit = format_duration(sec)
        print(f"{sec} seconds is {duration_magnitude} {duration_unit}.")