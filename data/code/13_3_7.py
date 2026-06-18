from datetime import datetime
from typing import List

def calculate_elapsed_time(timestamps: List[str]) -> float:
    """
    Calculates the total elapsed time in seconds between the earliest 
    and latest timestamp provided as ISO 8601 strings.
    
    Args:
        timestamps (List[str]): A list of ISO 8601 formatted datetime strings.
        
    Returns:
        float: The duration in seconds between min and max timestamps.
        Raises ValueError if the input is empty or contains unparseable dates.
    """
    if not timestamps:
        raise ValueError("Input list cannot be empty.")

    parsed_dates = []
    
    for ts_str in timestamps:
        try:
            # ISO 8601 format typically includes 'Z' at the end, so we strip it 
            # as Python's default parser expects a specific format.
            clean_ts = ts_str.replace('Z', '+00:00') if len(ts_str) > 3 else ts_str
            parsed_date = datetime.fromisoformat(clean_ts)
        except ValueError as e:
            raise ValueError(f"Unable to parse timestamp '{ts_str}': {str(e)}") from e
        
        parsed_dates.append(parsed_date)

    min_timestamp = min(parsed_dates)
    max_timestamp = max(parsed_dates)
    
    elapsed_delta = max_timestamp - min_timestamp
    
    return elapsed_delta.total_seconds()

if __name__ == '__main__':
    sample_timestamps = [
        "2023-10-01T10:00:00",
        "2023-10-05T14:30:00",
        "2023-10-06T08:15:00"
    ]

    elapsed_seconds = calculate_elapsed_time(sample_timestamps)
    
    print(f"The total elapsed time between the earliest and latest timestamp is {elapsed_seconds} seconds.")