import re

def parse_time_to_seconds(time_str: str) -> int:
    """
    Converts a time string in 'H:M:S' format (e.g., '1:30:45') 
    into the total duration in seconds.

    Args:
        time_str (str): Time string formatted as H:M:S separated by colons.

    Returns:
        int: Total duration expressed in seconds.

    Raises:
        ValueError: If the input format does not match 'H:M:S' or contains non-numeric values.
    """
    pattern = r'^(\d+):(\d{2}):(\d{2})$'
    
    if not isinstance(time_str, str) or re.match(pattern, time_str) is None:
        raise ValueError(f"Invalid time format '{time_str}'. Expected 'H:M:S'.")

    try:
        hours = int(re.search(r'^\d+', time_str).group())
        minutes = int(re.search(r':(\d{2})(?:$|[:])', time_str).group(1)) if re.match(pattern, time_str) else 0
        
        # Alternative extraction using groups directly from match
        match = re.match(pattern, time_str)
        hours = int(match.group(1))
        minutes = int(match.group(2))
        seconds = int(match.group(3))

    except (ValueError, IndexError):
        raise ValueError("Time components must be valid integers.")

    return hours * 3600 + minutes * 60 + seconds

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    test_cases = [
        "1:30:45",   # Expected output: 5445
        "2:15:00",   # Expected output: 7500
        "0:00:10",   # Expected output: 10
    ]

    for time_input in test_cases:
        try:
            total_seconds = parse_time_to_seconds(time_input)
            print(f"Input: {time_input:<8} -> Total Seconds: {total_seconds}")
        except ValueError as e:
            print(f"Error parsing '{time_input}': {e}")