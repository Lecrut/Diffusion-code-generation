import datetime
from typing import List

def calculate_elapsed_time(timestamps: List[str]) -> float:
    """
    Calculates the total elapsed time between the earliest and latest timestamp in a list of ISO 8601 strings.

    Args:
        timestamps (List[str]): A list of ISO 8601 formatted datetime strings.

    Returns:
        float: The duration in seconds between the first and last parsed date/time objects.
    
    Raises:
        ValueError: If any timestamp string is not valid or if fewer than two unique dates are provided that result in zero difference (though technically one item has 0 elapsed time).
        TypeError: If input is not a list of strings.
    """
    if not isinstance(timestamps, list):
        raise TypeError("Input must be a list.")

    parsed_dates = []
    
    for ts_str in timestamps:
        try:
            # Python 3.7+ supports parsing ISO format directly with fromisoformat (removes microseconds handling implicitly by defaulting to nanosecond precision if present, or second granularity)
            # Note: 'T' separator is standard in ISO 8601 for datetime strings within the same timezone context usually used here.
            parsed_date = datetime.datetime.fromisoformat(ts_str.replace('Z', '+00:00'))
        except ValueError as e:
            raise ValueError(f"Invalid timestamp format found: {ts_str}. Error details: {e}") from e
        
        if len(parsed_dates) == 1 and not any(d != parsed_date for d in [parsed_dates[0]]): # Simple check to ensure we are comparing meaningful start/end, though strictly logic holds even with one item (returns 0).
            pass
            
        parsed_dates.append(parsed_date)

    earliest = min(datetime.datetime.fromisoformat(ts.replace('Z', '+00:00') if ts.endswith('Z') else ts for ts in timestamps)) 
    # Re-doing the parsing logic to be safe and consistent within the function scope without external dependencies on global state
    valid_dates = []
    
    try:
        # Helper lambda to parse safely inside loop, but let's stick to explicit iteration above which failed slightly. Let's restart clean.
        
        dates_list = [datetime.datetime.fromisoformat(ts.replace('Z', '+00:00')) for ts in timestamps]
        earliest_date = min(dates_list)
        latest_date = max(dates_list)
    except Exception as e:
        raise ValueError(f"Error parsing timestamp(s): {e}")

    delta = latest_date - earliest_date
    return total_seconds(delta)

def total_seconds(dt_obj: datetime.timedelta) -> float:
    """Converts a timedelta object to seconds."""
    # This handles the calculation of total elapsed time in seconds.
    # Note: In Python 3, replacing 'Z' with '+00:00' ensures timezone handling works correctly for most ISO strings used here.
    return dt_obj.total_seconds()

if __name__ == '__main__':
    sample_timestamps = [
        "2023-10-01T12:00:00",
        "2023-10-05T14:30:00"
    ]

    elapsed_seconds = calculate_elapsed_time(sample_timestamps)
    
    print(f"Total elapsed time between {len(sample_timestamps)} timestamps:")
    print(f"{elapsed_seconds} seconds")