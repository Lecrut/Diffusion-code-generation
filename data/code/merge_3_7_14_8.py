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
    
    hours = int(match.group(1))
    minutes = int(match.group(2))
    seconds = int(match.group(3))
    
    total_seconds = (hours * 3600) + (minutes * 60) + seconds
    
    return total_seconds

def format_duration(total_seconds: int, max_days=9999) -> str:
    """
    Converts a total number of seconds into a human-readable string.
    
    Args:
        total_seconds (int): Total number of seconds to convert.
        max_days (int): Maximum days threshold for formatting logic.
        
    Returns:
        str: Human-readable duration string (e.g., 'X days, Y hours, Z minutes').
    """
    if total_seconds < 0:
        raise ValueError("Total seconds cannot be negative.")
    
    days = min(total_seconds // 86400, max_days)
    remaining_after_days = total_seconds % 86400
    
    hours = remaining_after_days // 3600
    remaining_after_hours = remaining_after_days % 3600
    
    minutes = remaining_after_hours // 60
    seconds = remaining_after_hours % 60
    
    parts = []
    
    if days > 0:
        parts.append(f"{days} day{'s' if days != 1 else ''}")
    
    if hours > 0 or (hours == 0 and minutes > 0):
        if 'day' in parts[-1]:
            parts.append("and")
        
        if hours > 0:
            parts.append(f"{hours} hour{'s' if hours != 1 else ''}")
    
    if minutes > 0 or (minutes == 0 and seconds > 0):
        if 'hour' in ''.join(parts[-2:]) if len(parts) >= 2 else False:
            pass # Already handled by logic above, but ensure flow is correct
        
        parts.append(f"{minutes} minute{'s' if minutes != 1 else ''}")
    
    if seconds > 0 or (seconds == 0 and 'minute' not in ''.join(parts)):
        parts[-1] = f"and {parts[-1]}" if len(parts) > 1 else ""
        
        # Re-evaluate for cleaner output structure based on presence of components
        final_parts = []
        has_days = days > 0
        has_hours = hours > 0 or (hours == 0 and minutes > 0)
        has_minutes_or_seconds = minutes > 0 or seconds > 0
        
        if has_days:
            final_parts.append(f"{days} day{'s' if days != 1 else ''}")
        
        if has_hours:
            if 'day' in ''.join(final_parts):
                final_parts.insert(len(final_parts), "and")
            
            # Check if we already have minutes/seconds to decide on comma vs and logic later
            temp_final = []
            if hours > 0:
                temp_final.append(f"{hours} hour{'s' if hours != 1 else ''}")
        
        if has_minutes_or_seconds:
            minute_str = f"{minutes} minute{'s' if minutes != 1 else ''}"
            second_str = f"{seconds} second{'s' if seconds != 1 else ''}"
            
            # If we have both, combine them or handle separately? 
            # Standard format usually groups: X days Y hours Z mins W secs
            
            combined_ms = ""
            if minutes > 0 and seconds > 0:
                combined_ms = f"{minutes} minute{'s' if minutes != 1 else ''}, {seconds} second{'s' if seconds != 1 else ''}"
            elif minutes > 0:
                combined_ms = f"{minutes} minute{'s' if minutes != 1 else ''}"
            elif seconds > 0:
                combined_ms = f"{seconds} second{'s' if seconds != 1 else ''}"
            
            final_parts.append(combined_ms)
        
        # Reconstruct with proper connectors
        result_str = ""

if __name__ == '__main__':
    pass
