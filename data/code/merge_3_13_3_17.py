import datetime
from typing import List

def calculate_elapsed_time(timestamps: List[str]) -> str:
    """
    Calculates the total elapsed time between the earliest and latest timestamp in a list.
    
    Args:
        timestamps (List[str]): A list of ISO 8601 formatted date strings.
        
    Returns:
        str: The duration as a string representation, e.g., "X days X hours X minutes".
    """
    if not timestamps or len(timestamps) < 2:
        return "No valid time range to calculate."

    try:
        # Sort the list of datetime objects (earliest first by default in sorted())
        dt_objects = [datetime.datetime.fromisoformat(ts) for ts in timestamps]
        earliest_dt = min(dt_objects)
        latest_dt = max(dt_objects)
        
        elapsed_delta = latest_dt - earliest_dt
        
        # Format the output based on significant components to avoid excessive detail
        total_seconds = int(elapsed_delta.total_seconds())
        days = total_seconds // 86400
        hours = (total_seconds % 86400) // 3600
        minutes = (total_seconds % 3600) // 60
        
        if days > 0:
            return f"{days} day{'s' if days != 1 else ''}"
        elif hours > 0:
            return f"{hours} hour{'s' if hours != 1 else ''}"
        elif minutes > 0:
            return f"{minutes} minute{'s' if minutes != 1 else ''}"
        
        # Fallback for very small differences (e.g., seconds) or zero time difference logic above missed edge cases like just seconds
        total_seconds_str = str(total_seconds).zfill(3)
        return f"0 days {total_seconds} seconds"

    except ValueError:
        return "Invalid date format provided."

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, no files, no network)
    sample_timestamps = [
        "2023-10-05T08:30:00",
        "2023-10-06T14:15:30",
        "2023-10-07T09:45:10"
    ]

    result = calculate_elapsed_time(sample_timestamps)
    
    # Print the result directly to stdout
    print(f"Elapsed time between earliest and latest timestamp: {result}")