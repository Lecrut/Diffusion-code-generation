import re

def parse_time_to_seconds(time_str: str) -> int:
    """
    Converts a time string in 'HH:MM:SS' format to total seconds.
    
    Args:
        time_str (str): A string representing hours, minutes, and seconds separated by colons.
        
    Returns:
        int: Total number of seconds represented by the input string.
        
    Raises:
        ValueError: If the input does not match 'HH:MM:SS' format.
    """
    pattern = r'^(\d{2}):(\d{2}):(\d{2})$'
    if not re.match(pattern, time_str):
        raise ValueError(f"Invalid time format '{time_str}'. Expected HH:MM:SS.")
    
    hours, minutes, seconds = map(int, time_str.split(':'))
    
    return (hours * 3600) + (minutes * 60) + seconds

def convert_seconds_to_readable(seconds: int) -> str:
    """
    Converts total seconds into a human-readable string format.
    The output includes days, hours, minutes if they are non-zero; otherwise it shows the 
    largest unit with non-zero value down to seconds.
    
    Args:
        seconds (int): Total number of seconds.
        
    Returns:
        str: Human-readable time string.
    """
    days = 0
    hours = 0
    minutes = 0
    
    if seconds < 0:
        raise ValueError("Seconds cannot be negative.")

    remaining_seconds = seconds
    
    # Calculate full days
    day_count, rem = divmod(remaining_seconds, 86400)  # 24 * 3600

if __name__ == '__main__':
    pass
