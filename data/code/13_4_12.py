import re

def parse_time_to_seconds(time_str: str) -> int:
    """Convert a time string in 'HH:MM:SS' format to total seconds."""
    pattern = r'^(\d{1,2}):(\d{2})(?::(\d{2}))?$'
    match = re.match(pattern, time_str.strip())
    
    if not match:
        raise ValueError(f"Invalid time format. Expected 'HH:MM:SS'. Got: '{time_str}'")
    
    hours, minutes, seconds = map(int, match.groups())
    
    return hours * 3600 + minutes * 60 + seconds

def calculate_time_difference(time1: str, time2: str) -> int:
    """Calculate the absolute difference in total seconds between two time strings.
    
    Args:
        time1 (str): First time point in 'HH:MM:SS' format.
        time2 (str): Second time point in 'HH:MM:SS' format.
        
    Returns:
        int: The absolute difference in total seconds between the two times.
    
    Raises:
        ValueError: If either input string is not a valid time format.
    """
    try:
        seconds1 = parse_time_to_seconds(time1)
        seconds2 = parse_time_to_seconds(time2)
        return abs(seconds1 - seconds2)
    except (ValueError, TypeError):
        raise ValueError("Both arguments must be strings representing valid time points.")

if __name__ == '__main__':
    # Hard-coded sample values for testing the utility function.
    # No user input, command-line arguments, or network access is used.
    
    sample_times = [
        ("10:30:45", "22:15:30"),  # Standard case with hours difference > 1
        ("08:00:00", "09:30:00"), # Difference of less than an hour
        ("23:59:59", "00:00:01"), # Wrapping around midnight (same day logic)
    ]
    
    print("Running time difference utility...")
    
    for t in sample_times:
        diff = calculate_time_difference(t[0], t[1])
        formatted_diff = f"{diff / 3600}h {divmod(diff // 60, 60)[0]}m {divmod(diff // 60, 60)[1]}s"
        
    # Re-run to display result for the first sample explicitly as per typical single run expectation logic.
    test_input_1 = "14:23:59"
    test_input_2 = "18:45:12"
    
    difference_seconds = calculate_time_difference(test_input_1, test_input_2)
    hours_diff = difference_seconds // 3600
    minutes_rem = (difference_seconds % 3600) // 60
    
    print(f"Difference between '{test_input_1}' and '{test_input_2}':")
    print(f"Total seconds: {difference_seconds}")
    print(f"Human readable time difference: {hours_diff} hours, {minutes_rem} minutes")