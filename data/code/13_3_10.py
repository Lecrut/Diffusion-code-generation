import datetime
from typing import List

def calculate_total_elapsed_time(timestamps: List[str]) -> float:
    """
    Calculates the total elapsed time in seconds between the earliest 
    and latest timestamp provided as ISO 8601 strings.

    Args:
        timestamps (List[str]): A list of datetime strings formatted as ISO 8601.

    Returns:
        float: The elapsed time in seconds. If no timestamps are provided, returns 0.0.
               Raises ValueError if a timestamp string is not valid or empty input.
    """
    if not timestamps:
        return 0.0
    
    try:
        sorted_timestamps = sorted(timestamps)
        
        # Parse the first (earliest) and last (latest) timestamps
        earliest_dt = datetime.datetime.fromisoformat(sorted_timestamps[0])
        latest_dt = datetime.datetime.fromisoformat(sorted_timestamps[-1])
        
        elapsed_seconds = abs((latest_dt - earliest_dt).total_seconds())
        return elapsed_seconds
        
    except ValueError as e:
        raise ValueError(f"Invalid timestamp format provided: {e}")

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    sample_timestamps = [
        "2023-10-05T14:30:00",
        "2023-10-06T09:15:30",
        "2023-10-07T18:45:00"
    ]

    result = calculate_total_elapsed_time(sample_timestamps)
    
    print(f"The total elapsed time is {result} seconds.")