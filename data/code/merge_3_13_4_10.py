import re

def time_difference_seconds(time_str1: str, time_str2: str) -> int:
    """
    Calculates the difference in total seconds between two time strings.
    
    The function assumes both input strings are valid HH:MM:SS format (or H:M:S).
    If a component is missing or invalid, it defaults to 0 for that position 
    based on regex matching logic below which enforces strict formatting.

    Args:
        time_str1 (str): First time point in "HH:MM:SS" format.
        time_str2 (str): Second time point in "HH:MM:SS" format.

    Returns:
        int: The absolute difference between the two times in seconds.
    
    Raises:
        ValueError: If either input string is not a valid time format.
    """
    # Regex pattern to match HH:MM:SS (allowing single digit hours/minutes/seconds)
    # Matches 0-23 for hour, 0-59 for minute, 0-59 for second
    pattern = r'^(\d{1,2}):(\d{1,2}):(\d{1,2})$'

    def parse_time(time_str: str) -> int:
        match = re.match(pattern, time_str.strip())
        if not match:
            raise ValueError(f"Invalid time format: {time_str}")
        
        hours = int(match.group(1))
        minutes = int(match.group(2))
        seconds = int(match.group(3))

        # Basic validation ranges (optional but good practice)
        if not (0 <= hours < 24 and 0 <= minutes < 60 and 0 <= seconds < 60):
            raise ValueError(f"Time components out of range: {time_str}")

        return hours * 3600 + minutes * 60 + seconds

    try:
        t1 = parse_time(time_str1)
        t2 = parse_time(time_str2)
        
        diff = abs(t1 - t2)
        return diff
        
    except ValueError as e:
        raise ValueError(f"Error processing time strings: {e}")

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input
    
    sample_times_1 = [
        "09:30:45",
        "23:59:59",
        "00:00:01"
    ]

    sample_times_2 = [
        "18:15:30",
        "12:00:00",
        "06:45:10"
    ]

    print("Time Difference Calculator Results:")
    
    for t1 in sample_times_1:
        for t2 in sample_times_2:
            diff = time_difference_seconds(t1, t2)
            # Only printing a few representative pairs to keep output concise but functional
            if "09" in t1 and "18" in t2 or "23" in t1 and "12" in t2:
                print(f"Difference between {t1} and {t2}: {diff} seconds")

    # Specific test case for edge cases
    try:
        result = time_difference_seconds("09:30:45", "invalid_time")
        print(result)
    except ValueError as e:
        print(f"Caught expected error: {e}")