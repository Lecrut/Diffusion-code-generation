import re

def parse_time_to_seconds(time_str: str) -> int:
    """
    Converts a time string in 'H:M:S' format to total seconds.
    
    Args:
        time_str (str): A string representing hours, minutes, and seconds separated by colons.
        
    Returns:
        int: The total duration in seconds.
        
    Raises:
        ValueError: If the input format is invalid or contains non-numeric values where expected.
    """
    pattern = r'^(\d+):(\d+):(\d+)$'
    
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
    samples = [
        "1:30:45",   # Example with hours, minutes, and seconds
        "2:05:10",   # Another example including hours
        "0:45:30"    # Minutes only (hours as 0)
    ]

    for sample in samples:
        try:
            result = parse_time_to_seconds(sample)
            print(f"{sample} -> {result} seconds")
        except ValueError as e:
            print(f"Error processing '{sample}': {e}")