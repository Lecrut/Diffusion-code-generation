import datetime
from typing import List

def calculate_total_elapsed_time(timestamps: List[str]) -> float:
    """
    Calculates the total elapsed time in seconds between the earliest 
    and latest timestamp provided as ISO 8601 strings.
    
    Args:
        timestamps (List[str]): A list of ISO 8601 formatted date-time strings.
        
    Returns:
        float: The duration in seconds between the first and last timestamp.
              Returns 0.0 if fewer than two unique valid dates are provided.
    """
    try:
        parsed_dates = []
        for ts_str in timestamps:
            # Handle both naive and aware datetimes (though ISO usually implies timezone or UTC)
            dt_obj = datetime.datetime.fromisoformat(ts_str.replace('Z', '+00:00'))
            if not isinstance(dt_obj, datetime.datetime):
                raise ValueError(f"Invalid date format for timestamp: {ts_str}")
            parsed_dates.append(dt_obj)
        
        # Sort the dates to find earliest and latest
        sorted_dates = sorted(parsed_dates)
        
        if len(sorted_dates) < 2:
            return 0.0
        
        start_time = min(sorted_dates)
        end_time = max(sorted_dates)
        
        elapsed_seconds = (end_time - start_time).total_seconds()
        return float(elapsed_seconds)
    
    except ValueError as e:
        # In a real scenario, we might log this error. Here we just re-raise 
        # or handle it gracefully by returning 0 to prevent crashing the script silently.
        print(f"Error processing timestamps: {e}", file=__import__('sys').stderr)
        return 0.0

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, files, or network access)
    sample_timestamps = [
        "2023-10-05T14:30:00",
        "2023-10-06T09:15:30.123456+00:00",
        "2023-10-07T23:59:59Z"
    ]

    result = calculate_total_elapsed_time(sample_timestamps)
    
    # Output the result directly to stdout without any markdown or extra text
    print(f"Total elapsed time between timestamps: {result} seconds")