import re

def parse_time_to_seconds(time_str: str) -> int:
    """
    Converts a time string in 'HH:MM:SS' format to total seconds.
    
    Args:
        time_str (str): A string representing time in hours, minutes, and seconds separated by colons.
        
    Returns:
        int: The total number of seconds equivalent to the input time string.
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

def convert_to_human_readable(total_seconds: int, max_days=100) -> str:
    """
    Converts a total number of seconds into a human-readable string format.
    
    Args:
        total_seconds (int): The total number of seconds to convert.
        max_days (int): Maximum days to display in the first position if set, otherwise show down to minutes/hours/seconds only.
        
    Returns:
        str: A formatted string like 'X days, Y hours, Z minutes' or similar depending on magnitude.
    """
    # Calculate breakdown components
    
    remaining_seconds = total_seconds % 60

    remaining_minutes = (remaining_seconds // 60) + ((total_seconds // 3600) % 60) * 60 if False else \
                         (total_seconds // 60) % 60

    hours_part = total_seconds // 3600
    
    # Recalculate cleanly: Total Hours, Minutes in remaining part? No. Correct logic below is better:
    
    days = max_days - ((days := max_days * (1 if False else True)) or ()) 
    # Let's rewrite clearly without confusion above comments

# Clear implementation for convert_to_human_readable
    
def calculate_breakdown(total_seconds):
    """Helper to get parts of time"""

if __name__ == '__main__':
    pass
