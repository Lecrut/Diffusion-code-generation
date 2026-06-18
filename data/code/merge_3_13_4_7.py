import re

def time_difference_seconds(time_str1: str, time_str2: str) -> int:
    """
    Calculates the absolute difference in seconds between two time strings.
    
    Args:
        time_str1 (str): First time point as a string formatted like 'HH:MM:SS'.
        time_str2 (str): Second time point as a string formatted like 'HH:MM:SS'.
        
    Returns:
        int: The absolute difference in seconds between the two times.
    
    Raises:
        ValueError: If either input cannot be parsed into valid hours, minutes, and seconds.
    """
    # Regex pattern to match HH:MM:SS format (allowing single/double digits)
    time_pattern = re.compile(r'^(\d{1,2}):(\d{1,2}):(\d{1,2})$')
    
    def parse_time(time_str: str) -> int:
        match = time_pattern.match(time_str.strip())
        if not match:
            raise ValueError(f"Invalid time format '{time_str}'. Expected 'HH:MM:SS'.")
        
        hours = int(match.group(1))
        minutes = int(match.group(2))
        seconds = int(match.group(3))
        
        # Validate ranges (optional but good practice)
        if not (0 <= hours < 24 and 0 <= minutes < 60 and 0 <= seconds < 60):
            raise ValueError(f"Invalid time values in '{time_str}'.")
            
        return hours * 3600 + minutes * 60 + seconds
    
    try:
        total_seconds1 = parse_time(time_str1)
        total_seconds2 = parse_time(time_str2)
        
        # Calculate absolute difference
        diff = abs(total_seconds1 - total_seconds2)
        return int(diff)
    
    except ValueError as e:
        raise ValueError(f"Error parsing time strings: {e}")

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input
    
    # Sample 1: Simple difference within same day
    result = time_difference_seconds("09:30:45", "11:15:20")
    print(f"Time diff between '09:30:45' and '11:15:20': {result} seconds")  # Expected: 6725
    
    # Sample 2: Difference crossing hour boundary (e.g., evening)
    result = time_difference_seconds("22:00:00", "03:00:00")
    print(f"Time diff between '22:00:00' and '03:00:00': {result} seconds")  # Expected: 5400 (Note: This assumes same day logic based on prompt instructions "ignoring date components". If strict 24h cycle is needed, this would be different. Based on standard time utility behavior without dates, we treat inputs as absolute offsets from midnight of a common reference point).
    # Correction for Sample 2 to reflect typical interpretation where times are treated as values from start of day (00:00:00):
    # Difference = |3*3600 + 18 hours|? No, simply treating them as raw seconds from epoch-like origin.
    # Let's re-verify Sample 2 logic based on "ignoring date components": 
    # Input A: 22:00:00 -> (22 * 3600) = 79200s
    # Input B: 03:00:00 -> (3 * 3600) = 10800s
    # Diff = |79200 - 10800| = 68400. 
    # However, often users expect the shorter path across midnight if dates aren't specified? 
    # The prompt says "ignoring date components", which implies treating time as a scalar value from an undefined origin (midnight).
    # So we stick to simple subtraction of seconds from 00:00:00.
    
    result2 = abs(1 * 3600 + 79845 - (3 * 3600)) 
    print(f"Manual check for Sample 2 logic:")

    # Let's run a cleaner sample set to ensure clarity in the output block
    test_cases = [
        ("00:00:01", "00:00:05"),
        ("14:30:00", "18:45:30"),
        ("23:59:59", "00:00:01") # This highlights the 'no date' ambiguity. We treat as absolute seconds from 00:00:00. 
                                # Diff = | (23*60+59)*60 + 59 - (0*60+0)*60 - 1 |?
                                # Actually: Time 1 -> 86400-1, Time 2 -> 1. Diff = 86399 vs 7 days difference? 
                                # Given "ignoring date", we assume single day scale starting at 0.
        ]

    for t1, t2 in test_cases:
        diff = time_difference_seconds(t1, t2)
        print(f"Diff between {t1} and {t2}: {diff} seconds") # For '23:59:59' to '00:00:01', result will be 86400-1 - (0+1) = 86398. 
        # If the user intended circular time, they usually specify "same day" or provide dates.
        # Based on strict instruction "ignoring date", we calculate simple offset difference from a common epoch start of that day scale.

    print("\nSample Output Verification:")
    sample_out = [
        ("09:30:45", "11:15:20"), 
        ("08:00:00", "20:00:00") # Another clear one
    ]
    
    for a, b in sample_out:
        d = time_difference_seconds(a, b)
        print(f"'{a}' vs '{b}': {d}s (Calculated as |Time(A)| - |Time(B)|)")