import datetime

def calculate_elapsed_time(timestamps):
    """
    Calculates the total elapsed time between the earliest and latest timestamp in a list of ISO 8601 strings.
    
    Args:
        timestamps (list[str]): List of ISO 8601 formatted date-time strings.
        
    Returns:
        int: Elapsed time in seconds as an integer.
    """
    if not timestamps:
        return 0
    
    # Sort the list to ensure we process from earliest to latest
    sorted_timestamps = sorted(timestamps)
    
    try:
        first_dt = datetime.datetime.fromisoformat(sorted_timestamps[0])
        last_dt = datetime.datetime.fromisoformat(sorted_timestamps[-1])
        
        elapsed_delta = last_dt - first_dt
        
        # Return the result as a float representing seconds, or int if no fractional part exists.
        return int(elapsed_delta.total_seconds())
    except ValueError:
        raise ValueError("All timestamps must be valid ISO 8601 formatted strings.")

if __name__ == '__main__':
    sample_timestamps = [
        "2023-01-01T00:00:00",
        "2023-01-02T12:30:45",
        "2023-01-08T09:15:30"
    ]

    result = calculate_elapsed_time(sample_timestamps)
    
    print(f"Total elapsed time between earliest and latest timestamp: {result} seconds")