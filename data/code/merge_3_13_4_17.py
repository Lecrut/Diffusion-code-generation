import re

def time_difference_seconds(time_str1: str, time_str2: str) -> int:
    """
    Calculates the absolute difference in total seconds between two time strings.
    
    The function assumes standard HH:MM:SS format or allows flexible parsing 
    by extracting hours, minutes, and seconds using regex. It ignores date components
    as per requirements, focusing solely on the time scale of day 0 (24-hour cycle).

    Args:
        time_str1 (str): First time point in string format (e.g., "13:45:30").
        time_str2 (str): Second time point in string format.

    Returns:
        int: Absolute difference between the two times in seconds.
    
    Raises:
        ValueError: If either input does not match a recognizable time pattern.
    """
    # Regex to capture HH, MM, SS components allowing optional leading zeros or spaces
    pattern = r'^(\d{1,2}):\s*(\d{1,2})?:?\s*(\d{1,2})?$'
    
    def parse_time(time_str: str) -> int:
        match = re.match(pattern.strip(), time_str.strip())
        if not match:
            raise ValueError(f"Invalid time format for '{time_str}'. Expected HH:MM:SS")
        
        h, m, s = map(int, match.groups())
        return (h * 3600) + (m * 60) + s

    try:
        seconds1 = parse_time(time_str1)
        seconds2 = parse_time(time_str2)
        diff = abs(seconds1 - seconds2)
        
        # Ensure result stays within a single day's range if crossing midnight logic is implied, 
        # though standard subtraction suffices for simple difference.
        return diff
        
    except ValueError as e:
        raise e

if __name__ == '__main__':
    sample_times = ["13:45:30", "20:10:15"]
    
    try:
        result = time_difference_seconds(sample_times[0], sample_times[1])
        print(f"Difference between {sample_times[0]} and {sample_times[1]} is {result} seconds.")
        
        # Additional test cases for robustness without user input
        tests = [
            ("08:30:00", "09:45:00"),  # Simple difference
            ("23:59:59", "00:00:01"), # Crossing midnight (simple diff)
            ("12:00:00", "12:00:00")   # Zero difference
        ]
        
        for t1, t2 in tests:
            res = time_difference_seconds(t1, t2)
            print(f"Difference between {t1} and {t2}: {res}s")
            
    except Exception as e:
        if hasattr(e, 'args') and len(e.args) > 0:
            print(f"Error processing times: {e.args[0]}")
        else:
            print("An unexpected error occurred.")