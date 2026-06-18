import datetime

def calculate_elapsed_time(timestamps):
    """
    Calculates the total elapsed time between the earliest and latest timestamp in a list.
    
    Args:
        timestamps (list[str]): A list of ISO 8601 formatted date strings.
        
    Returns:
        int or float: The duration in seconds. If the result is less than one second, 
                     it returns an integer; otherwise, it returns a float to preserve precision.
    """
    if not timestamps:
        return 0
    
    # Sort timestamps to ensure we process them chronologically (though set/diff works regardless)
    sorted_timestamps = sorted(timestamps)
    
    try:
        earliest_dt = datetime.datetime.fromisoformat(sorted_timestamps[0])
        latest_dt = datetime.datetime.fromisoformat(sorted_timestamps[-1])
        
        delta = latest_dt - earliest_dt
        
        # Return seconds as int if whole number, else float for sub-second precision
        return delta.total_seconds()
    except ValueError:
        raise ValueError("All timestamps must be valid ISO 8601 strings.")

if __name__ == '__main__':
    sample_timestamps = [
        "2023-10-01T10:00:00",
        "2023-10-05T14:30:00",
        "2023-10-07T09:15:00"
    ]
    
    result = calculate_elapsed_time(sample_timestamps)
    print(f"The elapsed time between the earliest and latest timestamp is {result} seconds.")