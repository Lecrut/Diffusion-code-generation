from datetime import datetime, timedelta, timezone

def calculate_time_delta(dt1: datetime, dt2: datetime) -> timedelta:
    """
    Calculates the time difference between two timezone-aware datetime objects.

    Args:
        dt1 (datetime): The first date and time.
        dt2 (datetime): The second date and time.

    Returns:
        timedelta: A fixed-duration object representing the delta between the inputs.
    
    Note: This function assumes both input arguments are timezone-aware datetime objects.
          No external libraries or interactive prompts are used, ensuring standalone execution capability.
    """
    return dt1 - dt2

if __name__ == '__main__':
    # Sample hard-coded values
    base_time = datetime(2023, 10, 5, 14, 30, 0, tzinfo=timezone.utc)
    
    future_event = datetime(2023, 10, 6, 9, 15, 30, tzinfo=timezone(timezone.utc))
    
    result_delta = calculate_time_delta(base_time, future_event)

    print(f"Time Delta: {result_delta}")