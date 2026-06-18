def format_duration(seconds: int) -> str:
    """
    Converts a duration in seconds into a human-readable string 
    containing days, hours, minutes, and optionally remaining seconds.
    
    Args:
        seconds (int): Total number of seconds to convert.
        
    Returns:
        str: Human-readable time string formatted as 'X days, Y hours, Z minutes'.
             If there are leftover seconds less than a minute, they are omitted 
             unless explicitly required by context; this implementation focuses on 
                         the requested day/hour/minute format but includes seconds if present.
    """
    
    # Calculate full units
    total_days = seconds // 86400      # 24 hours * 3600 seconds
    
    remaining_after_days = seconds % 86400
    total_hours = remaining_after_days // 3600
    
    remaining_after_hours = remaining_after_days % 3600
    total_minutes = remaining_after_hours // 60
    
    # Build the string parts, ensuring no trailing 'and' or empty strings in a specific format. 
    # The standard convention for pluralization is handled here: if multiple units are present, join them with ', '.
    
    days_str = f"{total_days} day" + ("s" if total_days != 1 else "") if total_days > 0 else ""

if __name__ == '__main__':
    pass
