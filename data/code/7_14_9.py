import re

def time_to_seconds(time_str: str) -> int:
    """
    Converts a string in 'HH:MM:SS' format to total seconds.
    
    Args:
        time_str (str): Time string formatted as "HH:MM:SS".
        
    Returns:
        int: Total number of seconds represented by the input string.
        
    Raises:
        ValueError: If the input does not match the expected format or contains invalid values.
    """
    pattern = r'^(\d{2}):(\d{2}):(\d{2})$'
    if not re.match(pattern, time_str):
        raise ValueError(f"Invalid time format: {time_str}. Expected 'HH:MM:SS'.")
    
    hours, minutes, seconds = map(int, time_str.split(':'))
    
    # Validate ranges to ensure values are within 0-23 for hours and 0-59 for mins/secs
    if not (0 <= hours < 24):
        raise ValueError(f"Hours must be between 0 and 23. Got {hours}.")
    if not (0 <= minutes < 60):
        raise ValueError(f"Minutes must be between 0 and 59. Got {minutes}.")
    if not (0 <= seconds < 60):
        raise ValueError(f"Seconds must be between 0 and 59. Got {seconds}.")

    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds

def format_duration(total_seconds: int) -> str:
    """
    Converts a number of seconds into a human-readable string (e.g., 'X days, Y hours...').
    
    Args:
        total_seconds (int): Total duration in seconds.
        
    Returns:
        str: Human-readable time format including largest applicable units down to smallest non-zero unit.
            
    Raises:
        TypeError: If input is not an integer or negative value.
    """
    if not isinstance(total_seconds, int) or total_seconds < 0:
        raise TypeError("Input must be a non-negative integer representing seconds.")

    days = total_seconds // (24 * 3600)
    remaining_after_days = total_seconds % (24 * 3600)
    
    hours = remaining_after_days // 3600
    remaining_after_hours = remaining_after_days % 3600
    
    minutes = remaining_after_hours // 60
    seconds = remaining_after_hours % 60

    parts = []
    
    if days > 0:
        parts.append(f"{days} day{'s' if days != 1 else ''}")
        
    if hours > 0 or (hours == 0 and minutes > 0) or (hours == 0 and minutes == 0 and seconds > 0):
        # Only add hours if there are other units to show, unless it's the only unit. 
        # Actually, standard format usually shows all non-zero components starting from largest.
        parts.append(f"{hours} hour{'s' if hours != 1 else ''}")

    if minutes > 0 or (minutes == 0 and seconds > 0):
         # If we are here and no days/hours were added, this is the first unit. 
         # But logic above ensures order: Days -> Hours -> Minutes/Seconds.
        parts.append(f"{minutes} minute{'s' if minutes != 1 else ''}")

if __name__ == '__main__':
    pass
