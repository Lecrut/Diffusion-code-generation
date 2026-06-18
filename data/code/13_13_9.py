import re
from datetime import datetime

def parse_time_string(time_str):
    """
    Parses a single time string in ISO-like format (e.g., 'YYYY-MM-DDTHH:MM') 
    or similar consistent formats into a datetime object.
    
    This function attempts to match common time date patterns using regex,
    falling back to standard parsing if the pattern is not explicitly defined
    but looks like an absolute timestamp string.
    
    Args:
        time_str (str): A string representing a single time/datetime value.
        
    Returns:
        datetime or None: The parsed datetime object if successful, otherwise None.
    """
    # Try standard ISO 8601 with 'T' separator first as it's the most common "consistent format" for diffs
    try:
        return datetime.fromisoformat(time_str.replace('Z', '+00:00').replace('+00:00', ''))
    except ValueError:
        pass
    
    # Fallback to trying a generic date-time string with space or T separator if ISO fails, 
    # assuming the input format is consistent and likely follows YYYY-MM-DD HH:MM:ss pattern.
    try:
        return datetime.strptime(time_str.strip(), "%Y-%m-%d %H:%M")
    except ValueError:
        pass
    
    # Another common variation without seconds or with different separators, trying to be robust 
    # for the "consistent format" assumption by attempting a few standard strptime formats.
    patterns = [
        "%Y/%m/%d %H:%M",
        "%Y%m%d%H%M",
        "%d-%m-%y %H:%M",
        "%B %d, %Y at %I:%M %p"  # Less likely for diffs but covers text logs sometimes found in samples.
    ]
    
    for pattern in patterns:
        try:
            return datetime.strptime(time_str.strip(), pattern)
        except ValueError:
            continue
            
    return None

def calculate_net_time_difference(time_diffs_string):
    """
    Processes a string containing multiple time differences separated by a delimiter (e.g., ';') 
    and calculates the net time difference between the earliest and latest time points.
    
    Args:
        time_diffs_string (str): A string containing time values, e.g., "10:30; 20:45".
        
    Returns:
        int or float: The duration in seconds between the earliest and latest times parsed from the input.
                      If no valid times are found, returns None.
    """
    # Split string by delimiter (semicolon) and strip whitespace from each part
    parts = [part.strip() for part in time_diffs_string.split(';')]
    
    parseable_times = []
    
    # Filter out empty strings and attempt parsing for each valid part
    for part in parts:
        if not part or len(part) == 0:
            continue
            
        parsed_time = parse_time_string(part)
        
        if parsed_time is None:
            print(f"Warning: Could not parse time string '{part}'. Skipping.")
            # Depending on strictness, one might return an error here. 
            # For this efficient algorithm task, we skip invalid entries but log them.
            continue
            
        parseable_times.append(parsed_time)
    
    if len(parseable_times) < 2:
        print("Error: At least two valid time points are required to calculate a difference.")
        return None
    
    earliest = min(parseable_times)
    latest = max(parseable_times)
    
    # Calculate the delta in seconds (positive value representing net difference magnitude)
    duration_seconds = abs((latest - earliest).total_seconds())
    
    return int(duration_seconds)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements. 
    # These represent time points separated by a semicolon.
    sample_input = "2023-10-05 14:30; 2023-10-05 16:45"
    
    result_seconds = calculate_net_time_difference(sample_input)
    
    if result_seconds is not None:
        print(f"Net time difference calculated successfully.")
        print(f"Difference in seconds: {result_seconds}")
        
        # Optional conversion to hours for readability based on the sample data
        diff_minutes = abs(result_seconds // 60)
        diff_hours = int(diff_minutes / 60)
        remaining_mins = diff_minutes % 60
        
        if result_seconds > 0:
            print(f"Net time difference is {diff_hours} hour(s), {remaining_mins} minute(s).")
    else:
        print("Calculation failed or insufficient data.")