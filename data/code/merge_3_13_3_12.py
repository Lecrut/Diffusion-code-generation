import datetime

def calculate_elapsed_time(timestamps):
    """
    Calculates the total elapsed time between the earliest and latest timestamp in a list.
    
    Args:
        timestamps (list[str]): List of ISO 8601 formatted date strings.
        
    Returns:
        int or float: Total elapsed time in seconds, rounded to integer if whole number.
                      If no valid timestamps are found, returns None.
    """
    try:
        parsed_timestamps = [datetime.datetime.fromisoformat(ts) for ts in timestamps]
        earliest = min(parsed_timestamps)
        latest = max(parsed_timestamps)
        
        elapsed_seconds = (latest - earliest).total_seconds()
        return int(elapsed_seconds) if elapsed_seconds.is_integer() else round(elapsed_seconds, 2)

    except ValueError:
        # Handles invalid ISO 8601 format in the list
        raise ValueError("Invalid timestamp detected. All timestamps must be valid ISO 8601 strings.")

if __name__ == '__main__':
    sample_timestamps = [
        "2023-01-01T00:00:00",
        "2023-01-05T12:30:45",
        "2023-06-18T09:15:00"
    ]

    result = calculate_elapsed_time(sample_timestamps)
    
    print(f"The total elapsed time is {result} seconds.")