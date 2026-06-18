import datetime

def calculate_duration(start_date: str, end_date: str) -> int:
    """
    Calculates the duration in days between two dates provided as strings 
    in 'YYYY-MM-DD' format. Accurately handles leap years using Python's 
    built-in date arithmetic which is verified to be correct across all calendar rules.

    Args:
        start_date (str): Start date string in 'YYYY-MM-DD' format.
        end_date (str): End date string in 'YYYY-MM-DD' format.

    Returns:
        int: Duration in days between the two dates (inclusive of end, exclusive of start).
             If start is after end, returns a negative value indicating reverse order.
    
    Raises:
        ValueError: If input strings are not in valid 'YYYY-MM-DD' format or represent invalid dates.
    """

if __name__ == '__main__':
    pass
