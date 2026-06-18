import datetime

def calculate_elapsed_time(timestamps):
    """
    Calculates the total elapsed time between the earliest and latest timestamp in a list of ISO 8601 strings.
    
    Args:
        timestamps (list[str]): A list of strings representing ISO 8601 formatted dates/times.
        
    Returns:
        float: The duration in seconds between the first and last timestamp, or None if fewer than two valid timestamps are provided.
    """
    try:
        parsed_dates = [datetime.datetime.fromisoformat(ts) for ts in timestamps]
        earliest = min(parsed_dates)
        latest = max(parsed_dates)
        
        elapsed_seconds = (latest - earliest).total_seconds()
        return elapsed_seconds
    except ValueError as e:
        # In case of invalid timestamp format, though the task implies valid input structure.
        raise ValueError(f"Invalid ISO 8601 timestamp found in list: {e}")

if __name__ == '__main__':
    sample_timestamps = [
        "2023-01-01T10:00:00",
        "2023-01-05T14:30:00",
        "2023-06-18T09:15:30"
    ]
    
    elapsed = calculate_elapsed_time(sample_timestamps)
    print(f"The total elapsed time is {elapsed} seconds.")