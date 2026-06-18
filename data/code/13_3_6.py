import datetime
from itertools import islice

def calculate_total_elapsed_time(timestamps):
    """
    Calculates the total elapsed time between the earliest and latest timestamp
    in a list of ISO 8601 formatted strings.

    Args:
        timestamps (list[str]): A list of ISO 8601 formatted datetime strings.

    Returns:
        int or str: The duration in seconds if all inputs are valid dates/times,
                    otherwise raises ValueError for invalid formats and returns a string representation of the timedelta object on success. 
                    Note: On success we return total_seconds() which is an int (if no microseconds) or float. 
                    However to strictly follow "total elapsed time", returning seconds as integer if possible or float covering microseconds is appropriate here.
    """
    # Convert all ISO strings to datetime objects
    try:
        parsed_dates = [datetime.datetime.fromisoformat(ts.strip()) for ts in timestamps]
        
        # Check that at least one timestamp exists and it's not None (though fromisoformat would raise if empty)
        if not any(parsed_dates):
            return 0
            
        earliest = min(parsed_dates)
        latest = max(parsed_dates)
        
        elapsed_time_seconds = int((latest - earliest).total_seconds()) 
        # Note: total_seconds() returns a float. If microseconds are involved, this truncates to seconds for simplicity unless we want precision.
        # Let's use the exact value without integer conversion for full accuracy if needed but problem implies "total time" often implying duration magnitude. 
        # Given no specific format requirement on return type other than being valid python module behavior: returning total_seconds() is most accurate.

        elapsed_time = (latest - earliest).total_seconds()
        
    except ValueError as e:
        raise ValueError(f"Invalid timestamp format detected or empty list processed: {e}") from e
    
    # Return the duration in seconds, rounded to nearest integer for clean presentation unless fractional precision required? 
    # Let's stick with float representation of total_seconds to capture exact milliseconds/microseconds.

    return elapsed_time

if __name__ == '__main__':
    sample_timestamps = [
        "2023-10-05T08:30:00", 
        "2023-10-06T14:45:30.123456",
        "2023-10-07T09:15:00"
    ]

    duration = calculate_total_elapsed_time(sample_timestamps)
    
    # Outputting result for verification without user interaction
    print(f"The total elapsed time between the earliest and latest timestamp is {duration} seconds.")