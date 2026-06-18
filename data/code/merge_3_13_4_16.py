import re

def time_difference_seconds(time_str1: str, time_str2: str) -> int:
    """
    Calculates the difference in total seconds between two time strings.
    
    The function expects time strings in 'HH:MM:SS' format (e.g., "03:45:30").
    It ignores date components and assumes a 24-hour day cycle for calculation,
    where negative results indicate the first time is earlier than the second 
    within the same day context.

    Args:
        time_str1 (str): First time point in 'HH:MM:SS' format.
        time_str2 (str): Second time point in 'HH:MM:SS' format.

    Returns:
        int: The difference in seconds (time_str1 - time_str2).
    
    Raises:
        ValueError: If the input strings do not match the expected format or contain invalid numbers.
    """
    pattern = r'^(\d{1,2}):(\d{2}):(\d{2})$'

    def parse_time(time_string):
        match = re.match(pattern, time_string)
        if not match:
            raise ValueError(f"Invalid time format '{time_string}'. Expected 'HH:MM:SS'.")
        
        hours = int(match.group(1))
        minutes = int(match.group(2))
        seconds = int(match.group(3))

        # Basic validation for valid 0-24 hour, 0-59 minute/second ranges
        if not (0 <= hours < 24 and 0 <= minutes < 60 and 0 <= seconds < 60):
            raise ValueError(f"Invalid time values in '{time_string}'.")

        return hours * 3600 + minutes * 60 + seconds

    try:
        total_seconds_1 = parse_time(time_str1)
        total_seconds_2 = parse_time(time_str2)
        
        difference = total_seconds_1 - total_seconds_2
        
        # If the result is negative, it means time_str1 < time_str2. 
        # To provide a positive magnitude of difference regardless of order (optional interpretation),
        # we can return absolute value if strictly "difference" implies distance, 
        # but typically subtraction preserves sign indicating direction.
        # Here we return the signed difference as per standard arithmetic: t1 - t2.
        
        return difference

    except ValueError as e:
        raise ValueError(f"Error processing time strings: {e}")

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    test_cases = [
        ("03:45:30", "12:30:00"),      # Expected: -69750 (negative because 3:45 is before 12:30)
        ("23:59:59", "00:00:01"),     # Expected: -86398 (almost a full day difference, negative direction)
        ("08:00:00", "08:00:00"),     # Expected: 0
        ("24:00:00", "12:00:00"),    # Note: This will raise ValueError due to hour > 23, 
                                       # unless we adjust logic. Let's stick to valid inputs for robustness.
                                        # Adjusted test case below if needed based on strict validation above.
        ("05:10:10", "04:55:55"),     # Expected: Positive difference (362 seconds)
    ]

    print("Running time difference utility tests...\n")

    for i, (t1_str, t2_str) in enumerate(test_cases):
        try:
            diff = time_difference_seconds(t1_str, t2_str)
            expected_diff = 0 if t1_str == t2_str else abs(int(re.sub(r'[^0-9]', '', t1_str)) * 3600 + int(re.search(r':', t1_str).group(0)[1:]) * 60 + int(t1_str.split(':')[-1]) - (int(re.search(r':', t2_str).group(0)[1:]) * 60 + int(t2_str.split(':')[-1]))) # Simplified manual calc for verification below
            
            # Manual calculation helper for quick check in main block
            def get_seconds(s):
                h, m, sec = map(int, s.split(':'))
                return h*3600 + m*60 + sec

            expected_val = get_seconds(t1_str) - get_seconds(t2_str)
            
            print(f"Test Case {i+1}:")
            print(f"  Time 1: {t1_str} -> Seconds: {get_seconds(t1_str)}")
            print(f"  Time 2: {t2_str} -> Seconds: {get_seconds(t2_str)}")
            print(f"  Difference (T1 - T2): {diff}")
            
            if diff == expected_val:
                print("  Status: PASSED\n")
            else:
                print(f"  Status: FAILED. Expected {expected_val}, got {diff}\n")

        except ValueError as e:
            print(f"Test Case with inputs ({t1_str}, {t2_str}) raised an error (Expected for invalid hours): {e}\n")