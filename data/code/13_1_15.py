import datetime as dt

def calculate_time_delta(dt1: dt.datetime, dt2: dt.datetime) -> dt.timedelta:
    """
    Calculates the time difference between two timezone-aware datetime objects.

    Args:
        dt1 (datetime): The first timezone-aware datetime object.
        dt2 (datetime): The second timezone-aware datetime object.

    Returns:
        timedelta: A fixed-time delta representing the difference between dt1 and dt2.
                   If dt1 is earlier, a negative value or reverse order logic may apply depending on requirement,
                   but standard subtraction (dt1 - dt2) preserves sign relative to input order.
    """
    # Ensure both datetimes are in UTC before calculating difference for consistency across timezones
    utc_dt1 = dt1.astimezone(dt.timezone.utc) if hasattr(dt1, 'tzinfo') else None
    
    # If either datetime lacks timezone info (shouldn't happen per task description but safe guard), raise error
    if not isinstance(dt1.tzinfo, type(None)) and not isinstance(dt2.tzinfo, type(None)):
        utc_dt1 = dt1.astimezone(dt.timezone.utc)
        utc_dt2 = dt2.astimezone(dt.timezone.utc)

        return utc_dt1 - utc_dt2
    else:
            # Handle if inputs were already naive or one is missing (though task says timezone-aware, robustness helps)
         raise ValueError("Both datetime objects must be timezone-aware.")

if __name__ == '__main__':
    # Hard-coded sample values with explicit timezones
    tz = dt.timezone.utc
    
    start_dt = dt.datetime(2023, 10, 5, 10, 30, 45) + (dt.timedelta(hours=5),).replace(microseconds=-int(dt.time.min.microsecond)) # Simplified creation for clarity
    end_dt = dt.datetime.now(tz=tz)

    try:
        result_delta = calculate_time_delta(start_dt, end_dt)
        
        print(f"Time Delta between {start_dt.isoformat()} and {end_dt.isoformat()}:")
        print(result_delta.total_seconds())  # Output total seconds for demonstration
        
    except ValueError as e:
        print(f"Error occurred during calculation: {e}")