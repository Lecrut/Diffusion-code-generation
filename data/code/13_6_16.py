"""
Script to calculate the time difference in hours between two timezone definitions.
The logic assumes standard UTC offsets provided as inputs.
"""

def parse_timezone_offset(timezone_str: str) -> int:
    """
    Parses a timezone string like 'UTC+5', 'EST' (approximated for demo), or '-4' 
    into its integer hour offset from GMT/UTC.

    Since the requirement is to read definitions without external dependencies,
    we implement a robust parser that handles standard formats:
    - '+HH', '-HH', or just HH with optional colon separator (e.g., +0530)
    - Named timezones are mapped manually for this self-contained example.

    Args:
        timezone_str: String representation of the timezone offset or name.

    Returns:
        The integer hour difference from UTC. Raises ValueError if invalid format.
    """
    
    # Handle common named zones with fixed offsets relative to UTC (approximations)
    zone_mapping = {
        'UTC': 0,
        'GMT': 0,
        'EST': -5,
        'CST': -6,
        'MST': -7,
        'PST': -8,
        'JST': 9,
    }

    if timezone_str in zone_mapping:
        return zone_mapping[timezone_str]

    # Parse numeric offset formats like +5, -430, or just digits with sign
    normalized = timezone_str.lstrip("-+").replace(":", "")
    
    try:
        value = int(normalized)
        
        if normalized.startswith("+"):
            return value
        elif normalized.startswith("-"):
            return -value
        else:
            # Assume no separator, treat as integer directly (e.g., 5 -> +5)
            return value
            
    except ValueError:
        raise ValueError(f"Invalid timezone format: {timezone_str}")

def calculate_difference(tz1_def: str, tz2_def: str) -> int:
    """
    Calculates the difference in hours between two timezones.

    Args:
        tz1_def: Definition string for first timezone (e.g., 'UTC+5' or 'EST')
        tz2_def: Definition string for second timezone

    Returns:
        Integer representing hour difference (tz1 - tz2)
    """
    offset1 = parse_timezone_offset(tz1_def.strip())
    offset2 = parse_timezone_offset(tz2_def.strip())
    
    return offset1 - offset2

if __name__ == '__main__':
    # Hard-coded sample definitions without file I/O or user input
    
    config_data_1 = "UTC+5"      # India Standard Time (IST) base calculation for demo purpose here as +5h from UTC approx
    config_data_2 = "EST"       # Eastern Standard Time

    diff_hours = calculate_difference(config_data_1, config_data_2)
    
    print(f"Difference between {config_data_1} and {config_data_2}: {diff_hours:+d} hours")