import datetime
from typing import List

def calculate_total_elapsed_time(timestamps: List[str]) -> int:
    """
    Calculates the total elapsed time in seconds between the earliest 
    and latest timestamp provided as ISO 8601 strings.
    
    Args:
        timestamps (List[str]): A list of ISO 8601 formatted datetime strings.
        
    Returns:
        int: The elapsed time in seconds between the first and last timestamp.
    """
    if not timestamps or len(timestamps) < 2:
        raise ValueError("At least two timestamps are required to calculate elapsed time.")

    # Sort timestamps to ensure we get the earliest and latest correctly, 
    # although min/max functions handle this internally for comparison purposes.
    sorted_timestamps = sorted([datetime.datetime.fromisoformat(ts).replace(tzinfo=None) for ts in timestamps])
    
    start_time = sorted_timestamps[0]
    end_time = sorted_timestamps[-1]

    delta = end_time - start_time
    return int(delta.total_seconds())

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or external files)
    sample_data: List[str] = [
        "2023-10-01T08:30:00",
        "2023-10-05T14:45:30",
        "2023-10-06T09:15:00"
    ]

    try:
        elapsed_seconds = calculate_total_elapsed_time(sample_data)
        print(f"The total elapsed time is {elapsed_seconds} seconds.")
    except Exception as e:
        print(f"An error occurred while calculating the time: {e}")