from datetime import datetime, timedelta
import zoneinfo  # Python 3.9+; fallback to pytz logic if needed but standard lib preferred here

def calculate_time_delta(dt1: datetime, dt2: datetime) -> timedelta:
    """
    Calculates the time difference between two timezone-aware datetime objects.
    
    The function ensures both datetimes are interpreted in their respective 
    local times before calculating the delta, effectively normalizing them to 
    a common reference (UTC is used internally by Python's zoneinfo).

    Args:
        dt1 (datetime): First timezone-aware datetime object.
        dt2 (datetime): Second timezone-aware datetime object.

    Returns:
        timedelta: The difference between the two datetimes. Positive if dt2 > dt1, 
                   otherwise negative.
    
    Raises:
        ValueError: If either input is not a timezone-aware datetime.
    """
    # Ensure both are aware (this check handles cases where naive datetimes might slip through)
    assert dt1.tzinfo is not None and dt2.tzinfo is not None, "Both inputs must be timezone-aware."

    return dt2 - dt1

if __name__ == "__main__":
    # Sample values using different timezones (UTC+0, UTC-5) to demonstrate cross-timezone calculation.
    try:
        tz_utc = zoneinfo.ZoneInfo("Europe/London")  # Currently BST/UTC depending on season; fixed for demo clarity if needed but real TZ is best.
        tz_us_eastern = zoneinfo.ZoneInfo("America/New_York")

        dt_1 = datetime(2023, 5, 15, 14, 30, 0, tz_info=tz_utc) # May 15, 2023 at 14:30 BST (UTC+1 in summer for London)
        dt_2 = datetime(2023, 5, 15, 8, 30, 0, tz_info=tz_us_eastern) # Same day at 08:30 EST

        delta = calculate_time_delta(dt_1, dt_2)
        
        print(f"Time difference between {dt_1} and {dt_2}:")
        print(delta)
    except Exception as e:
        if hasattr(e, "args"):
            # Fallback for older Python versions or specific zoneinfo issues in restricted environments 
            # though standard lib supports this well.
            raise RuntimeError(f"Error calculating delta: {e}") from None
        else:
            raise