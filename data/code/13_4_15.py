import datetime

def time_difference_seconds(time1_str: str, time2_str: str) -> int:
    """
    Calculates the difference in total seconds between two time strings formatted as "HH:MM:SS".
    
    Args:
        time1_str (str): First time point string.
        time2_str (str): Second time point string.

    Returns:
        int: The absolute difference in seconds. Negative result indicates if we want order-dependent, 
             though typically differences are magnitude or t2 - t1 based on input logic below.
             
       Note: Assumes valid HH:MM:SS format where HH is 0-23 (for time only).

    Raises:
        ValueError: If either string cannot be parsed as a valid time.
    """

if __name__ == '__main__':
    pass
