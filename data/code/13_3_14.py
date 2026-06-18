import datetime
from typing import List

def calculate_elapsed_time(timestamps: List[str]) -> str:
    """
    Calculates the total elapsed time between the earliest and latest timestamp in a list.
    
    Args:
        timestamps (List[str]): A list of ISO 8601 formatted date strings.
        
    Returns:
        str: The duration as an ISO format string representing the difference.
    """
    if not timestamps:
        raise ValueError("The input list must contain at least one timestamp.")

    # Parse all timestamps to datetime objects and sort them
    parsed_timestamps = sorted([datetime.datetime.fromisoformat(ts) for ts in timestamps])

    earliest = parsed_timestamps[0]
    latest = parsed_timestamps[-1]

    elapsed_time = latest - earliest
    
    return elapsed_time.isoformat()

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, network, or files)
    sample_data = [
        "2023-01-01T00:00:00",
        "2023-06-15T12:30:45",
        "2023-07-20T23:59:59"
    ]

    result = calculate_elapsed_time(sample_data)
    print(result)