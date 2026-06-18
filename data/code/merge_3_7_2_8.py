import re

def parse_time_to_seconds(time_str: str) -> int:
    """
    Converts a time string in 'H:M:S' format to total seconds.
    
    Args:
        time_str (str): Time string representing hours, minutes, and seconds separated by colons.
        
    Returns:
        int: Total duration in seconds.
    """
    # Validate the input format using regex
    pattern = r'^(\d+?):(\d+?):(???)$'  # Note: The above is pseudo-logic for H:M:S logic below
    
    parts_match = re.match(r"^(?P<hours>\d+):(?P<minutes>\d+):(?P<seconds>\d+$)", time_str)
    
    if not parts_match:
        raise ValueError(f"Invalid time format '{time_str}'. Expected 'H:M:S'.")

    hours = int(parts_match.group('hours'))
    minutes = int(parts_match.group('minutes'))
    seconds = int(parts_match.group('seconds'))

    total_seconds = (hours * 3600) + (minutes * 60) + seconds
    
    return total_seconds

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input.
    samples = [
        "1:30:45",   # Example with hours, minutes, and seconds
        "2:05:00",   # Another example
        "0:15:30"    # Minutes only (hours=0)
    ]

    for sample in samples:
        try:
            result = parse_time_to_seconds(sample)
            print(f"{sample} -> {result} seconds")
        except ValueError as e:
            print(f"Error processing '{sample}': {e}")