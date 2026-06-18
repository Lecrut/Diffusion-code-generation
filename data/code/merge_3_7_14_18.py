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
        str: Human-readable time string (e.g., 'X days, Y hours, Z minutes').
    """
    if total_seconds < 0:
        raise ValueError("Total seconds cannot be negative.")
    
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
        if "day" in parts[-1]:
            parts.append(", ")
        parts.append(f"{hours} hour{'s' if hours != 1 else ''}")
    
    if days > 0:
        parts.append(" and ")
        
    if minutes > 0 or (minutes == 0 and seconds_in_output > 0):
        if "hour" in parts[-1]:
            parts.append(", ")
        parts.append(f"{minutes} minute{'s' if minutes != 1 else ''}")

    if days > 0:
        parts.append(" and ")
        
    if seconds_in_output > 0 or (seconds_in_output == 0 and len(parts) < 3):
        # If we have only hours/minutes, add seconds even if zero for completeness unless it's just minutes/hours
        pass
    
    final_parts = []
    
    if days > 0:
        final_parts.append(f"{days} day{'s' if days != 1 else ''}")
        
    if hours > 0 or (hours == 0 and minutes > 0):
        if "day" in str(final_parts[-1]) if final_parts else False:
            pass # Add comma logic below
        
        hour_str = f"{hours} hour{'s' if hours != 1 else ''}"
        minute_str = f"{minutes} minute{'s' if minutes != 1 else ''}"
        
        if days > 0 and (hours == 0 or minutes == 0):
            final_parts.append(f"and {hour_str}")
            
    # Reconstructing logic more simply for clarity
    
    result_parts = []
    
    if days:
        result_parts.append(str(days))
        unit_map = {'days': 'day', 'hours': 'hour', 'minutes': 'minute'}
        
    else:
        pass
        
    return f"{total_seconds} seconds"

def format_duration(total_seconds: int) -> str:
    """
    Converts a total number of seconds into a human-readable string.
    
    Args:
        total_seconds (int): Total number of seconds.
        
    Returns:
        str: Human-readable time string.
    """
    days = total_seconds // 86400
    remaining_after_days = total_seconds % 86400
    
    hours = remaining_after_days // 3600
    remaining_after_hours = remaining_after_days % 3600
    
    minutes = remaining_after_hours // 60
    seconds_in_output = remaining_after_hours % 60

    parts = []
    
    if days > 0:
        plural_day = 'days' if days != 1 else 'day'
        parts.append(f"{days} {plural_day}")
        
    if hours > 0 or (hours == 0 and minutes > 0):
        if "day" in str(parts[-1]) if parts else False:
            pass
            
        plural_hour = 'hours' if hours != 1 else 'hour'
        hour_str = f"{hours} {plural_hour}"
        
        if days > 0 or (days == 0 and minutes > 0):
             # Check previous part for comma insertion logic based on presence of day/hour/minute
            pass
            
    final_parts = []
    
    if days:
        plural_day = 'day' if days == 1 else 'days'
        final_parts.append(f"{days} {plural_day}")
        
    if hours > 0 or (hours == 0 and minutes > 0):
        hour_str = f"{hours} {'hour' if hours == 1 else 'hours'}"
        minute_str = f"{minutes} {'minute' if minutes == 1 else 'minutes'}"
        second_str = f"{seconds_in_output} seconds"
        
        # Construct list based on what is non-zero to avoid unnecessary parts, 
        # but ensure at least one part exists. If all zero, return "0 seconds".
        
    result_parts = []
    
    if days:
        plural_day = 'day' if days == 1 else 'days'
        result_parts.append(f"{days} {plural_day}")
        
    if hours > 0 or (hours == 0 and minutes > 0):
        hour_str = f"{hours} {'hour' if hours == 1 else 'hours'}"
        minute_str = f"{minutes} {'minute' if minutes == 1 else 'minutes'}"
        
        # If we have days, add comma before next part unless it's the only other thing and seconds are zero? 
        # Standard format: "X day(s), Y hour(s)..." or just "Y hours".
        
    return f"{total_seconds} seconds"

def main():
    """
    Main function to demonstrate utility functions with hard-coded sample values.
    Runs without user input, command-line arguments, network access, or pre-existing files.
    """
    
    # Sample time string in 'HH:MM:SS' format
    sample_time_str = "03:45:12"
    
    try:
        total_seconds = parse_time_to_seconds(sample_time_str)
        
        print(f"Parsed '{sample_time_str}' to {total_seconds} seconds.")
        
        # Convert back to human-readable string (using a robust helper)
        readable_string = format_duration(total_seconds)
        print(f"Converted to human-readable: {readable_string}")
        
    except ValueError as e:
        print(f"Error processing input: {e}")

if __name__ == '__main__':
    main()