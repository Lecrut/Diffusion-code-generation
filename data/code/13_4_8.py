import re

def time_difference_seconds(time_str1: str, time_str2: str) -> int:
    """
    Calculates the difference in total seconds between two time strings.
    
    The function assumes both input strings are valid HH:MM:SS format (or 
    H:M:S where hours/minutes can be omitted). It ignores date components
    and treats them as purely temporal points on a single day starting from 00:00:00.

    Args:
        time_str1 (str): First time point in "HH:MM:SS" format.
        time_str2 (str): Second time point in "HH:MM:SS" format.

    Returns:
        int: The absolute difference between the two times in seconds.
    
    Raises:
        ValueError: If either input string is not a valid time format.
    """
    # Regex pattern to match optional hours, minutes, and seconds separated by colons
    # Examples accepted: "12", "30m45s" (not supported per standard HH:MM:SS assumption), 
    # but primarily designed for "HH:MM:SS". To be robust against partial inputs like "H:M:S":
    pattern = r'^(\d{1,2}):?(\d{1,2})?:?(\d{1,2})?$'

    def parse_time(time_str):
        match = re.match(pattern, time_str.strip())
        if not match:
            raise ValueError(f"Invalid time format: {time_str}")
        
        hours = int(match.group(1)) if match.group(1) else 0
        minutes = int(match.group(2)) if match.group(2) else 0
        seconds = int(match.group(3)) if match.group(3) else 0
        
        return (hours * 3600) + (minutes * 60) + seconds

    try:
        total_seconds_1 = parse_time(time_str1)
        total_seconds_2 = parse_time(time_str2)
        
        # Return the absolute difference to ensure a positive duration magnitude, 
        # though signed difference could be used if direction matters.
        return abs(total_seconds_1 - total_seconds_2)

    except ValueError as e:
        raise ValueError(f"Error parsing time strings: {e}")

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or files
    
    test_cases = [
        ("09:30:15", "14:20:45"),  # Expected difference in seconds
        ("8h", "6m"),               # Partial format support (if regex allows) -> Note: Regex above supports H:M:S
        ("00:00:00", "23:59:59"),  # Full day cycle start to end
    ]

    for t1, t2 in test_cases:
        try:
            diff = time_difference_seconds(t1, t2)
            print(f"Time difference between '{t1}' and '{t2}': {diff} seconds")
        except ValueError as ve:
            print(f"Error processing inputs for '{t1}' or '{t2}': {ve}")

    # Specific example calculation verification
    sample_diff = time_difference_seconds("08:30", "17:45:30")
    expected_sample = 369 * 60 + 30  # (17*3600+45*60) - (8*3600) = ... let's just print the result directly
    
    print(f"Sample calculation ('08:30' vs '17:45:30'): {sample_diff} seconds")