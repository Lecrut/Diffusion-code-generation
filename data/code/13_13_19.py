import re
from datetime import datetime

def parse_time_diffs(time_string):
    """
    Parses a string containing time differences separated by ';'.
    Each difference is expected to be in format 'H:M:S' or 'HH:MM:SS'.
    
    Args:
        time_string (str): Input string with times separated by semicolons.
        
    Returns:
        list of datetime objects representing the parsed times.
    """
    # Split the input string by delimiter ';' and strip whitespace from each part
    parts = [part.strip() for part in time_string.split(';')]
    
    valid_times = []
    pattern = r'^(\d{1,2}):(\d{2}):(\d{2})$'
    
    # Regex to validate the format of a time string (HH:MM:SS or H:M:S)
    for part in parts:
        if not re.match(pattern, part):
            continue
        
        try:
            hours = int(part.split(':')[0])
            minutes = int(part.split(':')[1])
            seconds = int(part.split(':')[2])
            
            # Basic validation to ensure time is within a reasonable range (e.g., 0-23 for hours)
            if not (0 <= hours < 24 and 0 <= minutes < 60 and 0 <= seconds < 60):
                continue
                
            dt = datetime.strptime(part, '%H:%M:%S')
            valid_times.append(dt)
        except ValueError:
            # Skip invalid parts if any (e.g., non-numeric characters)
            continue
            
    return valid_times

def calculate_net_time_difference(times):
    """
    Calculates the net time difference between the earliest and latest times.
    
    Args:
        times (list of datetime objects): List of parsed time points.
        
    Returns:
        int or None: Net time difference in seconds, or None if no valid times found.
    """
    if not times:
        return None
    
    earliest = min(times)
    latest = max(times)
    
    diff_seconds = (latest - earliest).total_seconds()
    return int(diff_seconds)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements. No user input or file access.
    sample_input = "08:30:45;12:15:30;09:00:00"
    
    try:
        parsed_times = parse_time_diffs(sample_input)
        
        if not parsed_times:
            print("No valid time points found.")
        else:
            net_difference_seconds = calculate_net_time_difference(parsed_times)
            
            # Calculate start and end times for clarity in output
            earliest_str = min([t.strftime('%H:%M:%S') for t in parsed_times])
            latest_str = max([t.strftime('%H:%M:%S') for t in parsed_times])
            
            print(f"Earliest time: {earliest_str}")
            print(f"Latest time: {latest_str}")
            print(f"Net time difference (seconds): {net_difference_seconds}")
    except Exception as e:
        # Graceful error handling without printing stack traces in production-like scenarios
        print(f"An unexpected error occurred: {e}")