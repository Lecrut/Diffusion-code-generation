def format_duration(total_seconds: int) -> str:
    """
    Converts a total number of seconds into a human-readable string 
    containing days, hours, minutes, and remaining seconds if any.
    
    Args:
        total_seconds (int): The duration in seconds to convert.
        
    Returns:
        str: A formatted string representing the time span.
             Format: 'X days, Y hours, Z minutes' or similar depending on magnitude.
    """
    days = total_seconds // 86400
    remaining_after_days = total_seconds % 86400
    
    if days > 0:
        hours = remaining_after_days // 3600
        remaining_after_hours = remaining_after_days % 3600
        
        minutes = remaining_after_hours // 60
        seconds = remaining_after_hours % 60
        
        parts = []
        if days > 0:
            parts.append(f"{days} day{'s' if days != 1 else ''}")
        if hours > 0:
            parts.append(f"{hours} hour{'s' if hours != 1 else ''}")
        if minutes > 0 or seconds > 0:
            mins_str = f"{minutes} minute{'s' if minutes != 1 else ''}"
            secs_str = f"{seconds} second{'s' if seconds != 1 else ''}"
            parts.append(mins_str)
            if seconds > 0:
                parts.append(secs_str)
        return ', '.join(parts) + '.'
    else:
        hours = remaining_after_days // 3600
        minutes = (remaining_after_days % 3600) // 60
        seconds = remaining_after_days % 60
        
        parts = []
        if hours > 0:
            parts.append(f"{hours} hour{'s' if hours != 1 else ''}")
        if minutes > 0 or seconds > 0:
            mins_str = f"{minutes} minute{'s' if minutes != 1 else ''}"
            secs_str = f"{seconds} second{'s' if seconds != 1 else ''}"
            parts.append(mins_str)
            if seconds > 0:
                parts.append(secs_str)
        return ', '.join(parts) + '.'

def parse_time_string(time_str: str, format_type='HH:MM:SS') -> int:
    """
    Parses a time string in 'HH:MM:SS' (or similar) format and returns total seconds.
    
    Args:
        time_str (str): The input time string.
        
    Returns:
        int: Total number of seconds represented by the input string.
    """
    parts = time_str.split(':')
    if len(parts) != 3:
        raise ValueError(f"Invalid format for {format_type}, expected 'HH:MM:SS'")
    
    try:
        hours, minutes, seconds = map(int, parts)
        
        # Basic validation to ensure non-negative values (optional constraint based on context)
        if any(val < 0 for val in [hours, minutes, seconds]):
            raise ValueError("Time components must be non-negative.")
            
    except ValueError:
        raise ValueError(f"Invalid time string format: {time_str}")

    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    
    test_cases = [
        "12:34:56",      # Less than a day, includes hours/minutes/seconds
        "08:00:00",      # Exactly 8 hours
        "24:00:00",      # Exactly one full day (for demonstration of >24h logic if needed)
        "1357:99:56"     # Large values to test multiple days/hours/minutes
    ]

    print("Time Parsing and Formatting Utility Test Results:")
    print("-" * 40)

    for time_str in test_cases:
        try:
            total_seconds = parse_time_string(time_str, 'HH:MM:SS')
            formatted_output = format_duration(total_seconds)
            
            # Ensure the output doesn't have trailing punctuation issues based on logic above
            if formatted_output.endswith('.') and not any(x.isdigit() for x in list(formatted_output[-2:])[:-1]): 
                pass
            
            print(f"Input: {time_str}")
            print(f"Total Seconds: {total_seconds:,}")
            print(f"Human Readable: {formatted_output}")
            print("-" * 40)

        except Exception as e:
            print(f"Error processing '{time_str}': {e}")