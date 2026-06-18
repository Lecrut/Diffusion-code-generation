import math

def convert_to_appropriate_unit(total_seconds: int) -> tuple[int, str]:
    """
    Converts a total number of seconds into the most appropriate time unit.
    
    The logic prioritizes larger units to minimize decimal places and maximize integer precision where possible.
    Priority order (descending): Years > Months > Weeks > Days > Hours > Minutes > Seconds
    
    Returns:
        A tuple containing (value_in_unit, name_of_unit).
    """
    if total_seconds < 0:
        raise ValueError("Total seconds cannot be negative.")

    # Define unit durations in seconds and their display names for formatting
    units = [
        ("years", 31536000),   # Average year (365.25 days)
        ("months", 2629800),   # Approximate month (30.44 days based on calendar average)
        ("weeks", 604800),     # 7 * 24 * 3600
        ("days", 86400),       # 24 * 3600
        ("hours", 3600),       # 60 minutes per hour, etc. (Note: using standard definition)
        ("minutes", 60),
    ]

    for name, seconds_in_unit in units:
        if total_seconds >= seconds_in_unit:
            value = int(total_seconds / seconds_in_unit)
            remainder = total_seconds % seconds_in_unit
            
            # If there is a significant remainder (more than half the unit size), 
            # return both integer part and decimal representation for clarity.
            if remainder > 0:
                fraction = math.floor((remainder + seconds_in_unit / 2) / seconds_in_unit * 100) / 100
                value_formatted = f"{value}.{fraction}"
                return (float(value_formatted), name, total_seconds)
            
            # No significant remainder found for this unit or above
            return (int(total_seconds // sum(remaining)), name + "s" if remaining else name.capitalize(), total_seconds)

    raise ValueError("Time format not supported.")

def convert_to_appropriate_unit_v2(total_seconds: int) -> tuple[int, str]:
    """
    Simplified version of the conversion logic. Converts a total number of seconds 
    into the most appropriate time unit (years > months > weeks > days > hours > minutes).

    Returns:
        A tuple containing (value_in_unit, name_of_unit_str) where value is an integer if possible, else float.
        
    Example Output:
        If input 3601 -> ("1", "hours") or similar depending on remainder handling.
    
    """
    # Define unit durations in seconds and their display names for formatting

if __name__ == '__main__':
    pass
