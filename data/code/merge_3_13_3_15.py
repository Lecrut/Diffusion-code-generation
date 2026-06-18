import datetime
from typing import List

def calculate_total_elapsed_time(timestamps: List[str]) -> int:
    """
    Calculates the total elapsed time in seconds between the earliest 
    and latest timestamp provided as ISO 8601 strings.
    
    Args:
        timestamps (List[str]): A list of datetime string values in ISO 8601 format.
        
    Returns:
        int: The elapsed time in seconds between min and max timestamps.
    """
    if not timestamps or len(timestamps) < 2:
        return 0

    try:
        parsed_dates = [datetime.datetime.fromisoformat(ts.strip()) for ts in timestamps]
        earliest_date = min(parsed_dates)
        latest_date = max(parsed_dates)
        
        elapsed_seconds = int((latest_date - earliest_date).total_seconds())
        return elapsed_seconds
    except (ValueError, TypeError):
        raise ValueError("All input strings must be valid ISO 8601 datetime formats.")

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    sample_timestamps = [
        "2023-01-01T10:00:00",
        "2023-01-05T14:30:00",
        "2023-06-18T09:15:30"
    ]

    result = calculate_total_elapsed_time(sample_timestamps)
    
    print(f"The total elapsed time is {result} seconds.")