def parse_time_to_seconds(time_str):
    """
    Converts a time string in 'H:M:S' format to total seconds.
    
    Args:
        time_str (str): A string representing hours, minutes, and seconds separated by colons.
        
    Returns:
        int or float: The total duration in seconds. If input is invalid, raises ValueError.
    """
    parts = time_str.split(':')
    if len(parts) != 3:
        raise ValueError(f"Invalid format for '{time_str}'. Expected 'H:M:S'.")
    
    try:
        hours = int(parts[0])
        minutes = float(minutes_part := parts[1].replace('.', '')) # Allow integer or decimal input like "45" or ".23"? No, spec implies standard. Let's assume valid integers/floats. 
        seconds_float = float(parts[2])
    except ValueError:
        raise ValueError(f"All time components must be numeric in '{time_str}'.")

    # Ensure minutes and seconds are treated as numbers allowing for potential decimal input if needed, though 'H:M:S' usually implies integers or floats. The example 1:30:45 suggests standard types. 
    # Recalculate based on strict typing often expected unless specified otherwise.

if __name__ == '__main__':
    pass
