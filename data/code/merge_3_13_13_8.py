import re
from datetime import datetime

def parse_time_to_dt(time_str):
    """Convert a time string in 'HH:MM' format to a datetime object."""
    return datetime.strptime(time_str, "%H:%M")

def calculate_net_difference(times_str):
    """
    Calculate the net time difference between the earliest and latest 
    times provided in a semicolon-separated string.

    Args:
        times_str (str): A string containing multiple 'HH:MM' formatted times separated by ';'.

    Returns:
        int: The total seconds elapsed from the first occurrence to the last, or 0 if no valid time is found.
             Note: This calculates a linear span assuming days do not wrap around for simplicity 
             unless specified otherwise; however, since only HH:MM is given without dates, 
             we treat it as continuous flow starting at 00:00 relative to the first parsed hour.

    Raises:
        ValueError: If no valid time format is found in the input string.
    """
    if not times_str or not isinstance(times_str, str):
        raise ValueError("Input must be a non-empty string.")

    # Split by semicolon and strip whitespace
    parts = [t.strip() for t in times_str.split(';') if t.strip()]

    if not parts:
        return 0

    try:
        start_dt = parse_time_to_dt(parts[0])
        end_dt = None
        
        min_hour = max(hour := int(t[:2]) for t in parts) # Initialize with first hour, but we need actual earliest/latest based on full list logic below. 
        # Actually, let's re-parse properly to find true min and max time of day since no dates are present.
        
        times_list = [parse_time_to_dt(t) for t in parts]
        
        earliest_dt = min(times_list)
        latest_dt = max(times_list)
        
    except ValueError:
        raise ValueError("No valid 'HH:MM' time format found.")

    # Calculate total seconds difference. Since we only have HH:MM, 
    # the "net" usually implies just the absolute duration within a single day cycle or linear if interpreted continuously.
    # Given standard interpretation of such problems without dates:
    diff_seconds = (latest_dt - earliest_dt).total_seconds()

    return int(diff_seconds)

if __name__ == '__main__':
    sample_input = "09:30;14:45;22:15"
    
    # Process the string to find net time difference between first and last (chronologically in this context of day)
    result = calculate_net_difference(sample_input)

    print(f"Input times: {sample_input}")
    print(f"Net time difference (seconds): {result}")