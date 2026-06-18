import re

def parse_time_to_seconds(time_str: str) -> int:
    """
    Converts a time string in 'HH:MM:SS' format to total seconds.
    
    Args:
        time_str (str): Time string in 'HH:MM:SS' format.
        
    Returns:
        int: Total number of seconds represented by the input string.
    """
    pattern = r'^(\d{2}):(\d{2}):(\d{2})$'
    match = re.match(pattern, time_str)
    
    if not match:
        raise ValueError(f"Invalid time format '{time_str}'. Expected 'HH:MM:SS'.")
    
    hours, minutes, seconds = map(int, match.groups())
    
    total_seconds = (hours * 3600) + (minutes * 60) + seconds
    return total_seconds

def convert_to_human_readable(total_seconds: int) -> str:
    """
    Converts a number of seconds into a human-readable string format.
    Format includes days, hours, minutes if applicable; otherwise just the largest unit.
    
    Args:
        total_seconds (int): Total number of seconds to convert.
        
    Returns:
        str: Human-readable time string (e.g., 'X days, Y hours, Z minutes').
    """
    days = total_seconds // 86400
    remaining_after_days = total_seconds % 86400
    
    hours = remaining_after_days // 3600
    remaining_after_hours = remaining_after_days % 3600
    
    minutes = remaining_after_hours // 60
    seconds_in_output = remaining_after_hours % 60

    parts = []
    
    if days > 0:
        parts.append(f"{days} day{'s' if days != 1 else ''}")
        
    if hours > 0 or (hours == 0 and minutes > 0):
        if 'day' in parts[0]:
            parts.append(", ")
        parts.append(f"{hours} hour{'s' if hours != 1 else ''}")
            
    if minutes > 0:
        if ',' in ''.join(parts) or (len(parts) == 2 and any('hour' in p for p in parts)):
             pass # Already handled separator above, but ensure logic holds. 
             # Re-evaluating structure to be safe with commas.
        
    # Robust construction: build list then join with ', ' if multiple units exist
    output_parts = []
    
    if days > 0:
        output_parts.append(f"{days} day{'s' if days != 1 else ''}")
        
    if hours > 0 or minutes > 0:
        if len(output_parts) > 0 and (hours > 0):
            # If we have days, add comma before hours/minutes unless it's just the first part? 
            # Actually standard format is "X day(s), Y hour(s)...".
            pass
        
    final_list = []
    
    if days > 0:
        final_list.append(f"{days} day{'s' if days != 1 else ''}")
        
    if hours > 0 or minutes > 0:
        # If we have days, ensure comma separation for the next part(s)
        if len(final_list) == 1 and 'day' in final_list[0]:
            pass
            
        current_parts = []
        if hours > 0:
            current_parts.append(f"{hours} hour{'s' if hours != 1 else ''}")

if __name__ == '__main__':
    pass
