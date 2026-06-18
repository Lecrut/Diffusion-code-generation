import datetime
from typing import List

def calculate_elapsed_time(timestamps: List[str]) -> int:
    """
    Calculates the total elapsed time in seconds between the earliest 
    and latest timestamp provided as ISO 8601 strings.

    Args:
        timestamps (List[str]): A list of ISO 8601 formatted timestamp strings.

    Returns:
        int: The difference in seconds between the last and first date/time objects.
    
    Raises:
        ValueError: If no timestamps are provided or if a string cannot be parsed as datetime.
    """
    if not timestamps:
        raise ValueError("The list of timestamps must contain at least one element.")

    try:
        # Parse all strings into datetime objects and sort them to find min/max implicitly
        sorted_timestamps = [datetime.datetime.fromisoformat(ts) for ts in timestamps]
        
        earliest = sorted_timestamps[0]
        latest = sorted_timestamps[-1]
        
        elapsed_seconds = (latest - earliest).total_seconds()

    except ValueError as e:
        raise ValueError(f"Error parsing timestamp(s): {e}") from e
    
    return int(elapsed_seconds)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or network access.
    sample_timestamps = [
        "2023-10-05T14:30:00",
        "2023-10-06T10:15:30",
        "2023-10-07T09:00:00"
    ]

    try:
        result = calculate_elapsed_time(sample_timestamps)
        print(f"The elapsed time between the earliest and latest timestamp is {result} seconds.")
        
        # Optional debug info to show start/end times for clarity without cluttering main output too much if needed later.
        sorted_list = sorted([datetime.datetime.fromisoformat(ts) for ts in sample_timestamps])
        print(f"Earliest: {sorted_list[0]}")
        print(f"Latest:   {sorted_list[-1]}")
        
    except ValueError as ve:
        print(f"Error occurred while calculating elapsed time: {ve}")