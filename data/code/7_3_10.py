import re

def format_duration(duration_string: str) -> str:
    """
    Converts a time duration string in 'HH:MM:SS' format 
    into a human-readable string of Days, Hours, Minutes, Seconds.
    
    Args:
        duration_string (str): Time string in 'HH:MM:SS' format.
        
    Returns:
        str: Formatted string like "1 Day(s), 2 Hour(s), ...".
    """
    # Regex to match HH:MM:SS pattern with optional leading zeros or single digits
    time_pattern = r'^(\d{1,2}):(\d{1,2}):(\d{1,2})$'
    
    if not re.match(time_pattern, duration_string):
        raise ValueError(f"Invalid format. Expected 'HH:MM:SS', got '{duration_string}'")
        
    parts = [int(x) for x in duration_string.split(':')]
    hours, minutes, seconds = parts[0], parts[1], parts[2]

    total_seconds_in_day = 86400
    
    days = (hours * 3600 + minutes * 60 + seconds) // total_seconds_in_day
    remaining_hours = ((hours * 3600 + minutes * 60 + seconds)) % total_seconds_in_day

    hours_part = remaining_hours // 3600
    remaining_minutes = (remaining_hours - hours_part * 3600) / 60
    
    # Recalculate properly to avoid float issues for display but keep integer logic clean
    days = int(hours * 24 + minutes // 60) if hours > 1 else 1 if days == 0 and (hours or minutes or seconds) else 0

    # Clean up re-calculation with standard math approach:
    total_seconds = hours * 3600 + minutes * 60 + seconds
    
    actual_days = int(total_seconds // 86400)
    remaining_after_days = total_seconds % 86400

    final_hours = int(remaining_after_days // 3600)
    remaining_after_hours = (remaining_after_days - final_hours * 3600)
    
    final_minutes = int(remaining_after_hours / 60)
    actual_seconds = int(remaining_after_hours % 60)

    # Helper to format number with pluralization based on value and unit name
    def make_plural(unit: str, count: int):
        if count == 1:
            return f"{count} {unit}"
        else:
            return f"{int(count)} {unit}(s)"

    result_parts = []
    
    # Determine which components to include. 
    # If total is zero but string was provided, maybe show 0 for all? Or just skip if empty input logic isn't needed here.
    # Assuming valid non-negative inputs always have at least one unit potentially shown even if 0.

    result_parts.append(make_plural("Day", actual_days))
    
    if hours > 0 or days == 1: 
        result_parts.append(make_plural("Hour", final_hours))
        
    elif minutes > 0 and (days < 24): # Adjust logic to show only what matters after filtering out unnecessary zeros? No, just list all units.
         pass

    if hours > 0 or actual_days == 1: 
        result_parts.append(make_plural("Hour", final_hours))

if __name__ == '__main__':
    pass
