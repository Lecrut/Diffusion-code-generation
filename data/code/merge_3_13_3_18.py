import datetime

def calculate_elapsed_time(timestamps):
    """
    Calculates the total elapsed time between the earliest and latest timestamp in a list of ISO 8601 strings.
    
    Args:
        timestamps (list[str]): A list of ISO 8601 formatted date-time strings.
        
    Returns:
        datetime.timedelta: The duration between the first and last parsed timestamp.
        
    Raises:
        ValueError: If no timestamps are provided or if any string is not a valid ISO 8601 format.
    """
    if not timestamps:
        raise ValueError("The list of timestamps cannot be empty.")

    try:
        # Parse all timestamps to datetime objects and sort them by time value (though min/max handles order)
        parsed_timestamps = [datetime.datetime.fromisoformat(ts) for ts in timestamps]
        
        earliest = min(parsed_timestamps)
        latest = max(parsed_timestamps)
        
    except ValueError as e:
        raise ValueError(f"Invalid timestamp format found. Error details: {e}")

    return latest - earliest

if __name__ == '__main__':
    # Hard-coded sample values running without user input or external dependencies
    sample_data = [
        "2023-10-05T14:30:00",
        "2023-10-06T09:15:30.123456",
        "2023-10-07T18:45:00"
    ]

    elapsed = calculate_elapsed_time(sample_data)
    
    # Output the result in a human-readable format for verification
    print(f"Total elapsed time between earliest and latest timestamp: {elapsed}")