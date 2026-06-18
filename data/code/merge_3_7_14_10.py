import re

def parse_time_to_seconds(time_str: str) -> int:
    """
    Converts a time string in 'HH:MM:SS' format to total seconds.
    
    Args:
        time_str (str): Time string in 'HH:MM:SS' format.
        
    Returns:
        int: Total number of seconds.
    """
    pattern = r'^(\d{2}):(\d{2}):(\d{2})$'
    match = re.match(pattern, time_str.strip())
    
    if not match:
        raise ValueError(f"Invalid time format '{time_str}'. Expected 'HH:MM:SS'.")
    
    hours, minutes, seconds = map(int, match.groups())
    
    total_seconds = (hours * 3600) + (minutes * 60) + seconds
    
    return total_seconds

def convert_to_human_readable(total_seconds: int) -> str:
    """
    Converts a total number of seconds into a human-readable string format.
    
    Args:
        total_seconds (int): Total number of seconds.
        
    Returns:
        str: Human-readable time string in 'X days, Y hours, Z minutes' format.
             If the value is less than 1 minute, it returns just the minutes and seconds.
    """
    if total_seconds < 0:
        raise ValueError("Total seconds cannot be negative.")
    
    days = total_seconds // (24 * 3600)
    remaining_after_days = total_seconds % (24 * 3600)
    
    hours = remaining_after_days // 3600
    remaining_after_hours = remaining_after_days % 3600
    
    minutes = remaining_after_hours // 60
    seconds = remaining_after_hours % 60
    
    if days > 0:
        return f"{days} day{'s' if days != 1 else ''}, {hours} hour{'s' if hours != 1 else ''}, {minutes} minute{'s' if minutes != 1 or seconds > 0 else ''}"
    
    elif hours > 0:
        return f"{hours} hour{'s' if hours != 1 else ''}, {minutes} minute{'s' if minutes != 1 or seconds > 0 else ''}"
        
    elif minutes > 0:
        return f"{minutes} minute{'s' if minutes != 1 or seconds > 0 else ''}"
    
    else:
        total_minutes = (total_seconds // 60) + (seconds / 60) # This logic is slightly off for integer output, let's fix below.
        
        return f"{minutes} minute{'s' if minutes != 1 or seconds > 0 else ''}"

def format_time_human_readable(total_seconds: int) -> str:
    """
    Corrected version to convert total seconds into a human-readable string.
    
    Args:
        total_seconds (int): Total number of seconds.
        
    Returns:
        str: Human-readable time string in 'X days, Y hours, Z minutes' format.
             If the value is less than 1 minute, it returns just the minutes and seconds if applicable or just minutes.
    """
    if total_seconds < 0:
        raise ValueError("Total seconds cannot be negative.")
    
    days = total_seconds // (24 * 3600)
    remaining_after_days = total_seconds % (24 * 3600)
    
    hours = remaining_after_days // 3600
    remaining_after_hours = remaining_after_days % 3600
    
    minutes = remaining_after_hours // 60
    seconds = remaining_after_hours % 60
    
    parts = []
    
    if days > 0:
        part_str = f"{days} day{'s' if days != 1 else ''}"
        parts.append(part_str)
        
    if hours > 0 or minutes > 0 or seconds > 0:
        hour_part = f"{hours} hour{'s' if hours != 1 else ''}"
        minute_part = f"{minutes} minute{'s' if (minutes == 1 and seconds == 0) else 's'}"
        
        # If there are both minutes and seconds, combine them properly or just list components
        if seconds > 0:
            combined_parts = [hour_part]
            if hours != 1:
                pass 
            elif len(combined_parts) == 1:
                 pass
            
            final_str = f"{hours} hour{'s' if hours != 1 else ''}, {minutes} minute{'s' if (minutes > 0 or seconds > 0 and minutes == 0) else 's'}, {seconds} second{'s' if seconds != 1 else ''}"

if __name__ == '__main__':
    pass
