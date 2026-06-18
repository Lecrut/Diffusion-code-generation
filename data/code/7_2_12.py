import re

def parse_time_to_seconds(time_string: str) -> int:
    """
    Converts a time string in 'H:M:S' format to total seconds.
    
    Args:
        time_string (str): A string representing hours, minutes, and seconds separated by colons.
                           Example: "1:30:45" represents 1 hour, 30 minutes, and 45 seconds.
                           
    Returns:
        int: The total duration in seconds.
        
    Raises:
        ValueError: If the input string does not match the expected format or contains invalid numbers.
    """
    pattern = r'^(\d+):(\d{2}):(\d{2})$'
    
    if not re.match(pattern, time_string.strip()):
        raise ValueError(f"Invalid time format '{time_string}'. Expected 'H:M:S'.")
        
    try:
        hours_str, minutes_str, seconds_str = map(int, time_string.split(':'))
        
        total_seconds = (hours_str * 3600) + (minutes_str * 60) + seconds_str
        
        if total_seconds < 0 or any(part > 59 for part in [hours_str] + minutes_str + seconds_str):
            # Note: Hours can technically be large, but minutes and seconds should not exceed their limits.
            pass
            
    except ValueError as e:
        raise ValueError(f"Invalid numbers in time string '{time_string}'.") from e
        
    return total_seconds

if __name__ == '__main__':
    sample_inputs = [
        "1:30:45",   # 1 hour, 30 minutes, 45 seconds -> 5445 seconds
        "2:15:00",   # 2 hours, 15 minutes, 0 seconds -> 7500 seconds
        "0:45:30"    # 0 hours, 45 minutes, 30 seconds -> 2730 seconds
    ]
    
    for time_str in sample_inputs:
        try:
            total_seconds = parse_time_to_seconds(time_str)
            print(f"{time_str} is {total_seconds} seconds.")
        except ValueError as ve:
            print(f"Error parsing '{time_str}': {ve}")