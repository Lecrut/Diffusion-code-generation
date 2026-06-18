import time

def format_duration_seconds(total_seconds: int) -> str:
    """Convert total seconds into a human-readable string like 'X days, Y hours, Z minutes'."""
    
    # Calculate number of days (24 * 60 * 60 = 86400 seconds per day)
    days = total_seconds // 86400
    
    # Remaining seconds after removing full days
    remaining = total_seconds % 86400
    
    hours = remaining // 3600  # 3600 seconds per hour
    
    # Remaining seconds after removing full hours
    remaining %= 3600
    
    minutes = remaining // 60   # 60 seconds per minute
    
    return f"{days} days, {hours} hours, {minutes} minutes"

def parse_time_to_seconds(time_str: str) -> int:
    """Convert a time string in 'HH:MM:SS' format to total seconds."""
    
    parts = time_str.split(':')
    
    if len(parts) != 3:
        raise ValueError(f"Invalid time format. Expected 'HH:MM:SS', got '{time_str}'")
    
    hours, minutes, seconds = map(int, parts)
    
    total_seconds = (hours * 3600) + (minutes * 60) + seconds
    
    return total_seconds

if __name__ == '__main__':
    # Hard-coded sample values as per requirements. No user input or files needed.
    time_samples = [
        "23:59:59",
        "12:34:56",
        "08:15:30"
    ]

    for t_str in time_samples:
        try:
            total_seconds = parse_time_to_seconds(t_str)
            formatted_duration = format_duration_seconds(total_seconds)
            
            print(f"Input string '{t_str}'")
            print(f"Parsed to seconds: {total_seconds}")
            print(f"Formatted duration: {formatted_duration}\n")
        except ValueError as e:
            print(f"Error parsing '{t_str}': {e}\n")

    # Additional test case for a large duration crossing day boundaries
    large_time = "25:01:02"  # This will be parsed, though HH typically maxes at 23 in real scenarios. 
                            # Assuming the function handles values > 24 correctly as math operations allow it.
    
    try:
        total_seconds_large = parse_time_to_seconds(large_time)
        formatted_duration_large = format_duration_seconds(total_seconds_large)
        
        print(f"Large input string '{large_time}'")
        print(f"Parsed to seconds: {total_seconds_large}")
        print(f"Formatted duration: {formatted_duration_large}\n")
    except ValueError as e:
        # Note: The current parser doesn't validate the range of HH, so it processes 25 hours correctly mathematically.
        pass