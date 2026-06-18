import re

def time_to_total_seconds(time_str: str) -> int:
    """
    Converts a string in 'HH:MM:SS' format into total seconds.
    
    Args:
        time_str (str): A string representing hours, minutes, and seconds separated by colons.
        
    Returns:
        int: Total number of seconds represented by the input string.
        
    Raises:
        ValueError: If the input string does not match 'HH:MM:SS' format or contains invalid numbers.
    """
    pattern = r'^(\d{2}):(\d{2}):(\d{2})$'
    
    # Check if the string matches the expected format first (more robust than split later)
    parts = re.match(pattern, time_str.strip())
    if not parts:
        raise ValueError(f"Invalid time format '{time_str}'. Expected 'HH:MM:SS'.")

    hours = int(parts.group(1))
    minutes = int(parts.group(2))
    seconds = int(parts.group(3))

    # Basic validation for ranges (optional but good practice)
    if not (0 <= hours <= 99 and 0 <= minutes < 60 and 0 <= seconds < 60):
        raise ValueError(f"Invalid time components: '{time_str}'")

    return hours * 3600 + minutes * 60 + seconds

def total_seconds_to_duration(total_seconds: int) -> str:
    """
    Converts a total number of seconds into a human-readable string (e.g., 'X days, Y hours...').
    
    Args:
        total_seconds (int): The total count of seconds.
        
    Returns:
        str: A formatted string like "1 day(s), 2 hour(s)", etc.
    """
    if total_seconds < 0:
        raise ValueError("Total seconds cannot be negative.")

    days = total_seconds // 86400
    remaining = total_seconds % 86400
    
    hours = remaining // 3600
    remaining %= 3600
    
    minutes = remaining // 60
    final_remaining = remaining % 60

    # Build the list of non-zero components to avoid "1 day(s), 0 hour(s)" format unless necessary
    parts = []
    
    if days > 0:
        parts.append(f"{days} day{'s' if days != 1 else ''}(s)")
        
    if hours > 0:
        # Check again for the pluralization rule specifically before appending, 
        # though since we already processed days and subtracted, 'hours' here is strictly positive.
        parts.append(f"{hours} hour{'s' if hours != 1 else ''}(s)")

if __name__ == '__main__':
    pass
