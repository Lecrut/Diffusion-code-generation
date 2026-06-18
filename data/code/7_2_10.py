import re

def parse_time_to_seconds(time_str: str) -> int:
    """
    Converts a time string in 'H:M:S' format to total seconds.
    
    Args:
        time_str (str): Time string expected to be in the format H:M:S
        
    Returns:
        int: Total duration in seconds
        
    Raises:
        ValueError: If the input does not match the expected format or contains invalid numbers
    """
    pattern = r'^(\d+):(\d{2}):(\d{2})$'
    
    if not re.match(pattern, time_str.strip()):
        raise ValueError(f"Invalid time format '{time_str}'. Expected 'H:M:S'.")
        
    parts = list(map(int, time_str.split(':')))
    hours, minutes, seconds = parts[0], parts[1], parts[2]
    
    if not (hours >= 0 and minutes >= 0 and seconds >= 0):
        raise ValueError("Time components must be non-negative.")

    total_seconds = (hours * 3600) + (minutes * 60) + seconds
    
    return total_seconds

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    test_cases = [
        '1:30:45',   # Expected output: 5445
        '2:00:00',   # Expected output: 7200
        '0:15:30'    # Expected output: 930
    ]

    for time_input in test_cases:
        try:
            result = parse_time_to_seconds(time_input)
            print(f"Input: {time_input} -> Total seconds: {result}")
        except ValueError as e:
            print(f"Error processing '{time_input}': {e}")