import re

def time_difference_seconds(time_str1: str, time_str2: str) -> int:
    """
    Calculates the difference in total seconds between two time strings.
    
    The function assumes both input strings are valid HH:MM:SS format (or 
    H:M:S with optional leading zeros). Date components are ignored as per 
    task requirements, focusing solely on the time scale.

    Args:
        time_str1 (str): First time point in "HH:MM:SS" or similar format.
        time_str2 (str): Second time point in "HH:MM:SS" or similar format.

    Returns:
        int: The absolute difference between the two times in seconds.

    Raises:
        ValueError: If either input string is not a valid time format.
    """
    
    # Regex pattern to match HH:MM:SS, H:M:S formats (allowing optional leading zeros)
    # Matches 1-2 digits for hours/minutes/seconds separated by colons
    time_pattern = re.compile(r'^(\d{1,2}):(\d{1,2}):(\d{1,2})$')

    def parse_time(time_str: str) -> int:
        """Converts a valid time string to total seconds."""
        
        match = time_pattern.match(time_str.strip())
        if not match:
            raise ValueError(f"Invalid time format: {time_str}")
        
        hours, minutes, seconds = map(int, match.groups())
        
        # Validate ranges (0-23 for hours is standard, though task implies ignoring date)
        # Assuming 24-hour clock context as it's the most common for "HH" notation.
        if not (0 <= hours < 24):
            raise ValueError(f"Hours must be between 0 and 23: {hours}")
        
        return hours * 3600 + minutes * 60 + seconds

    try:
        total_seconds1 = parse_time(time_str1)
        total_seconds2 = parse_time(time_str2)
        difference = abs(total_seconds1 - total_seconds2)
        return difference
    except ValueError as e:
        raise ValueError(f"Error processing time strings: {e}")

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    test_cases = [
        ("10:30:45", "12:15:30"),  # Expected difference calculation
        ("09:00:00", "08:00:00"),  # Simple hour difference
        ("23:59:59", "00:00:00"),  # Crossing midnight (absolute diff)
    ]

    print("Running time difference utility tests...\n")
    
    for t1, t2 in test_cases:
        try:
            result = time_difference_seconds(t1, t2)
            print(f"Time A ({t1}) to Time B ({t2}): {result} seconds")
        except ValueError as ve:
            print(f"Error with inputs '{t1}' and '{t2}': {ve}")

    # Additional explicit test case for clarity
    sample_input = "05:45:30"
    sample_output_time = "06:10:15"
    
    diff = time_difference_seconds(sample_input, sample_output_time)
    print(f"\nSample Test:")
    print(f"{sample_input} to {sample_output_time}")
    print(f"Difference: {diff} seconds")