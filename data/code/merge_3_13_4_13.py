import re

def parse_time_to_seconds(time_str: str) -> int:
    """
    Parses a time string in 'HH:MM:SS' format into total seconds.
    
    Args:
        time_str (str): A string representing time in the format HH:MM:SS.
        
    Returns:
        int: The total number of seconds represented by the input string.
    """
    pattern = r'^(\d{2}):(\d{2}):(\d{2})$'
    match = re.match(pattern, time_str.strip())
    
    if not match:
        raise ValueError(f"Invalid time format '{time_str}'. Expected 'HH:MM:SS'.")
    
    hours, minutes, seconds = map(int, match.groups())
    
    total_seconds = (hours * 3600) + (minutes * 60) + seconds
    
    return total_seconds

def calculate_time_difference(time1_str: str, time2_str: str) -> int:
    """
    Calculates the absolute difference in seconds between two time points.
    
    Args:
        time1_str (str): First time string in 'HH:MM:SS' format.
        time2_str (str): Second time string in 'HH:MM:SS' format.
        
    Returns:
        int: The absolute difference in seconds between the two times.
    """
    try:
        seconds1 = parse_time_to_seconds(time1_str)
        seconds2 = parse_time_to_seconds(time2_str)
    except ValueError as e:
        raise ValueError(f"Error parsing time strings: {e}")

    return abs(seconds1 - seconds2)

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input.
    time_a = "03:45:30"
    time_b = "18:20:10"

    difference_seconds = calculate_time_difference(time_a, time_b)

    print(f"Difference between {time_a} and {time_b}: {difference_seconds} seconds")