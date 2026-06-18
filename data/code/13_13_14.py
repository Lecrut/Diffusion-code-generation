import re
from datetime import datetime

def parse_time_diff_string(time_diff_str: str) -> list[datetime]:
    """
    Parses a string containing multiple time differences separated by ';'.
    Each difference is expected to be in the format 'YYYY-MM-DD HH:MM' or similar.
    
    Args:
        time_diff_str (str): String with times separated by ';'
        
    Returns:
        list[datetime]: List of datetime objects representing parsed times
        
    Raises:
        ValueError: If a date/time string is invalid
    """
    # Split the input string by delimiter;
    if not isinstance(time_diff_str, str) or time_diff_str.strip() == '':
        return []

    parts = [part.strip() for part in time_diff_str.split(';') if part.strip()]
    
    times = []
    date_pattern = r'\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}'  # YYYY-MM-DD HH:MM
    
    for i, part in enumerate(parts):
        match = re.match(date_pattern, part)
        if not match:
            raise ValueError(f"Invalid date/time format at index {i}: '{part}'")
        
        try:
            dt = datetime.strptime(part, '%Y-%m-%d %H:%M')
            times.append(dt)
        except ValueError as e:
            raise ValueError(f"Failed to parse time component in part {i+1} due to error: {e}")

    return times

def calculate_net_time_diff(times: list[datetime]) -> datetime | None:
    """
    Calculates the net time difference between the earliest and latest time points.
    
    Args:
        times (list[datetime]): List of datetime objects
        
    Returns:
        datetime or None: The difference as a timedelta-like object represented 
                         by subtracting min from max, rounded to nearest minute if needed.
    """
    if not times:
        return None
    
    earliest = min(times)
    latest = max(times)
    
    # Calculate the net time difference (latest - earliest)
    diff_seconds = int((latest - earliest).total_seconds())
    
    # Round to nearest minute for cleaner output in some contexts, 
    # though timedelta is more precise. Here we return a simple representation.
    minutes_rounded = round(diff_seconds / 60) * 60
    
    from datetime import timedelta
    result_td = timedelta(seconds=minutes_rounded)
    
    return result_td

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, no files, etc.)
    sample_input_str = "2023-10-01 10:00;2023-10-05 14:30;2023-10-10 09:15"

    try:
        parsed_times = parse_time_diff_string(sample_input_str)
        
        if not parsed_times:
            print("No valid time points found.")
        else:
            net_difference = calculate_net_time_diff(parsed_times)
            
            # Format the output for clarity
            if isinstance(net_difference, timedelta):
                total_minutes = int(net_difference.total_seconds() / 60)
                hours, remainder = divmod(total_minutes, 60)
                
                print(f"Earliest time: {parsed_times[0]}")
                print(f"Latest time: {parsed_times[-1]}")
                print(f"Net Time Difference: {hours} hour(s), {remainder} minute(s)")
            else:
                print("Error calculating net difference.")

    except ValueError as e:
        print(f"Parsing error occurred: {e}")