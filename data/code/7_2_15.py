import re

def parse_time_to_seconds(time_str: str) -> int:
    """
    Converts a time string in 'H:M:S' format to total seconds.
    
    Args:
        time_str (str): A string representing hours, minutes, and seconds separated by colons.
        
    Returns:
        int: The total duration in seconds.
        
    Raises:
        ValueError: If the input format is invalid or contains non-numeric values where numbers are expected.
    """
    pattern = r'^(\d+):(\d{2}):(\d{2})$'
    
    match = re.match(pattern, time_str.strip())
    if not match:
        raise ValueError(f"Invalid time format '{time_str}'. Expected 'H:M:S'.")
        
    hours = int(match.group(1))
    minutes = int(match.group(2))
    seconds = int(match.group(3))
    
    total_seconds = (hours * 3600) + (minutes * 60) + seconds
    
    return total_seconds

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or command-line arguments.
    test_cases = [
        "1:30:45",   # Expected output: 5445
        "2:05:00",   # Expected output: 7500
        "0:10:30"    # Expected output: 630
    ]

    for time_input in test_cases:
        try:
            result = parse_time_to_seconds(time_input)
            print(f"{time_input} -> {result} seconds")
        except ValueError as e:
            print(f"Error processing '{time_input}': {e}")