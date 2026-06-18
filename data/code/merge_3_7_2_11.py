import re

def parse_time_to_seconds(time_str: str) -> int:
    """
    Converts a time string in 'H:M:S' format to total seconds.
    
    Args:
        time_str (str): A string representing hours, minutes, and seconds separated by colons.
        
    Returns:
        int: The total duration in seconds.
    """
    pattern = r'^(\d+):(\d{2}):(\d{2})$'
    match = re.match(pattern, time_str.strip())
    
    if not match:
        raise ValueError(f"Invalid time format '{time_str}'. Expected 'H:M:S'.")
    
    hours, minutes, seconds = map(int, match.groups())
    
    total_seconds = (hours * 3600) + (minutes * 60) + seconds
    return total_seconds

if __name__ == '__main__':
    # Hard-coded sample values as per requirements.
    test_cases = [
        '1:30:45',   # Example input
        '2:05:10',   # Another example with hours > 0 and minutes < 60
        '0:45:30'    # Minutes only case (hours=0)
    ]

    for time_input in test_cases:
        try:
            seconds = parse_time_to_seconds(time_input)
            print(f"Input '{time_input}' converted to {seconds} total seconds.")
        except ValueError as e:
            print(f"Error processing input '{time_input}': {e}")