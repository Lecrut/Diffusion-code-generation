import datetime
from zoneinfo import ZoneInfo

def calculate_time_delta(dt1: datetime.datetime, dt2: datetime.datetime) -> datetime.timedelta:
    """
    Calculate the time difference between two timezone-aware datetime objects.
    
    The function ensures both datetimes are in UTC before calculating the 
    absolute delta to handle any positive or negative intervals correctly.

    Args:
        dt1 (datetime.datetime): First timezone-aware datetime object.
        dt2 (datetime.datetime): Second timezone-aware datetime object.

    Returns:
        datetime.timedelta: Absolute time difference between dt1 and dt2 in UTC.
    """
    # Ensure both are converted to naive UTC datetimes by removing the timezone info after conversion
    utc_dt1 = dt1.astimezone(ZoneInfo("UTC")).replace(tzinfo=None)
    utc_dt2 = dt2.astimezone(ZoneInfo("UTC")).replace(tzinfo=None)

    return abs(datetime.timedelta(seconds=(utc_dt2 - utc_dt1).total_seconds()))

if __name__ == '__main__':
    # Sample data: New York and London timezones on a specific day
    ny_local = datetime.datetime(2023, 5, 19, 14, 0)
    london_utc_offset = ZoneInfo("America/New_York")
    
    # Create timezone-aware datetimes directly using the provided string inputs logic implicitly via zoneinfo
    dt_new_york: datetime.datetime | None = None

    try:
        dt_aware_ny = datetime.datetime(2023, 5, 19, 14, 0).astimezone(london_utc_offset)
        
        # Let's construct them properly for clarity in the sample block without external input files or prompts
        
        ny_dt = datetime.datetime(2023, 5, 19, 14, 0)
        tz_ny = ZoneInfo("America/New_York")
        
        london_dt = datetime.datetime(2023, 5, 19, 22, 0)
        tz_london = ZoneInfo("Europe/London")

        dt_aware_ny = ny_dt.replace(tzinfo=tz_ny)
        dt_aware_lon = london_dt.replace(tzinfo=tz_london)

    except Exception as e:
        print(f"Error creating datetimes: {e}")
        exit(1)

    delta = calculate_time_delta(dt_aware_ny, dt_aware_lon)
    
    # Output the result in a formatted string for verification purposes only (no console input needed)
    total_seconds = int(delta.total_seconds())
    print(f"Time difference: {delta}")
    print(f"Difference in seconds: {total_seconds}")