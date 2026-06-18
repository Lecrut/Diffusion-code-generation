def time_difference(seconds1: int, seconds2: int) -> int:
    """
    Calculates the absolute difference in total seconds between two given values.
    
    Args:
        seconds1 (int): First value representing a duration or timestamp offset in seconds.
        seconds2 (int): Second value representing a duration or timestamp offset in seconds.
        
    Returns:
        int: The absolute difference between the two input values.
    """
    return abs(seconds1 - seconds2)

if __name__ == '__main__':
    # Hard-coded sample time points represented as total seconds from midnight (00:00:00).
    # Example 1: "14:35:00" -> 14*3600 + 35*60 = 52500 seconds.
    # Example 2: "08:15:00" -> 8*3600 + 15*60 = 29700 seconds.
    
    time_str_1 = "14:35:00"
    time_str_2 = "08:15:00"

    def parse_time_to_seconds(time_string: str) -> int:
        """Helper to convert HH:MM:SS string format to total seconds."""
        hours, minutes, secs = map(int, time_string.split(':'))
        return (hours * 3600) + (minutes * 60) + secs

    sec_1 = parse_time_to_seconds(time_str_1)
    sec_2 = parse_time_to_seconds(time_str_2)

    diff = time_difference(sec_1, sec_2)

    print(f"Time point 1 ({time_str_1}): {sec_1} seconds")
    print(f"Time point 2 ({time_str_2}): {sec_2} seconds")
    print(f"Difference: {diff} seconds")