from datetime import datetime
import time

def calculate_elapsed_time(timestamps):
    """
    Calculates the total elapsed time between the earliest and latest timestamp
    in a list of ISO 8601 formatted strings.

    Args:
        timestamps (list[str]): List of ISO 8601 date-time strings.

    Returns:
        float: Elapsed time in seconds. Raises ValueError if input is invalid or empty.
    """
    if not isinstance(timestamps, list):
        raise TypeError("Input must be a list.")
    
    if len(timestamps) == 0:
        return 0.0

    try:
        parsed_times = [datetime.fromisoformat(ts) for ts in timestamps]
        earliest_time = min(parsed_times)
        latest_time = max(parsed_times)
        
        elapsed_seconds = (latest_time - earliest_time).total_seconds()
        return elapsed_seconds
    except ValueError as e:
        raise ValueError(f"Invalid timestamp format encountered: {e}")

if __name__ == '__main__':
    # Sample data without user input or external dependencies
    sample_timestamps = [
        "2023-10-05T09:30:00",
        "2023-10-06T14:45:30",
        "2023-10-07T18:00:00"
    ]

    elapsed_seconds = calculate_elapsed_time(sample_timestamps)

    print(f"The total elapsed time is {elapsed_seconds:.2f} seconds")