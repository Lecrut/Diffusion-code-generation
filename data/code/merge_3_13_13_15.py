import re
from datetime import datetime

def parse_time_diffs(time_string: str) -> list[datetime]:
    """
    Parses a string containing time differences separated by ';' 
    or ', ' and returns a sorted list of datetime objects representing the absolute times.
    
    Assumes input format is relative to midnight (e.g., "09:30;14:45, 23:00").
    If negative values are present in the string representation (unlikely for time points), 
    they would represent durations before midnight which we treat as absolute times here.
    
    The function handles common delimiters and formats.
    """
    # Normalize separators to a single space or semicolon if mixed, but primarily split by ';', ', '
    # We will replace any non-alphanumeric separator with a standard one for robustness 
    # assuming the input is well-formed as per task description (consistent format).
    
    # Split by common time delimiters: ';' and ', '
    parts = re.split(r'[;, ]+', time_string.strip())
    
    times = []
    for part in parts:
        if not part:
            continue
        
        try:
            dt_str = part.strip()
            # Parse the datetime. Assuming format HH:MM or similar consistent with standard time strings.
            # We assume a 24-hour clock and that the input is just "HH:MM". 
            # If seconds are needed, they would be appended if present in the specific format used.
            dt = datetime.strptime(dt_str, "%H:%M")
            times.append(dt)
        except ValueError as e:
            raise ValueError(f"Invalid time format found: {part}. Error details: {e}")

    return sorted(times)

def calculate_net_difference(time_points: list[datetime]) -> int | float:
    """
    Calculates the net time difference (in seconds) between the earliest and latest 
    datetime in the provided list. Returns 0 if fewer than two points exist or empty list.
    
    Args:
        time_points: Sorted list of datetime objects
        
    Returns:
        Integer representing total seconds difference, or float for precision handling if needed.
    """
    if len(time_points) < 2:
        return 0
    
    earliest = min(time_points)
    latest = max(time_points)
    
    delta_seconds = (latest - earliest).total_seconds()
    return int(delta_seconds)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements. No user input or external files used.
    sample_input_str = "09:30;14:45, 23:00"

    try:
        time_points_list = parse_time_diffs(sample_input_str)
        
        if not time_points_list:
            print("No valid time points found.")
        else:
            net_seconds = calculate_net_difference(time_points_list)
            
            # Formatting output for clarity, though the task asks to return a single runnable module.
            earliest_time = min(time_points_list).strftime("%H:%M")
            latest_time = max(time_points_list).strftime("%H:%M")
            
            print(f"Earliest time: {earliest_time}")
            print(f"Latest time: {latest_time}")
            print(f"Net difference in seconds: {net_seconds}")

    except ValueError as e:
        print(f"Error processing input: {e}")